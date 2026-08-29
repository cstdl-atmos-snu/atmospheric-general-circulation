"""Small helpers shared by the course notebooks.

Data access is through NOAA PSL's OPeNDAP server for the NCEP/NCAR Reanalysis 1,
which needs no registration. See https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html
"""
import numpy as np
import xarray as xr

PSL = "https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived"
PSL_HTTP = "https://downloads.psl.noaa.gov/Datasets/ncep.reanalysis.derived"


def open_ncep_ltm(var, level_type="pressure", period="1991-2020"):
    """Open the monthly long-term-mean climatology of an NCEP/NCAR R1 variable.

    var: 'uwnd', 'vwnd', 'air', 'hgt', 'omega', 'shum', ... (see PSL catalogue)
    level_type: 'pressure' or 'surface'
    Tries OPeNDAP first, then falls back to an HTTP download into ./data/.
    """
    fname = f"{var}.mon.ltm.{period}.nc"
    try:
        ds = xr.open_dataset(f"{PSL}/{level_type}/{fname}")
    except OSError:
        import os, urllib.request
        os.makedirs("data", exist_ok=True)
        local = os.path.join("data", fname)
        if not os.path.exists(local):
            urllib.request.urlretrieve(f"{PSL_HTTP}/{level_type}/{fname}", local)
        ds = xr.open_dataset(local)
    # The 'time' axis of the ltm files is a dummy year; replace it with month numbers.
    if "time" in ds.dims and ds.sizes["time"] == 12:
        ds = ds.assign_coords(time=np.arange(1, 13)).rename(time="month")
    return ds


def zonal_mean(da, lon="lon"):
    """Zonal average [A] along the longitude axis."""
    return da.mean(lon)


def season_mean(da, months, dim="month"):
    """Average over a list of months, e.g. [12, 1, 2] for DJF."""
    return da.sel({dim: months}).mean(dim)
