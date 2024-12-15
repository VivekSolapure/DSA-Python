import netCDF4 as nc

# Open the NetCDF file
dataset = nc.Dataset(r'C:\Users\solap\Downloads\nrt_global_al_phy_l3_1hz_20240801_20240822.nc')

# Print the contents of the file
print(dataset)
