# how to use uv
- use uv run to run python scripts or module
- use uv add to add package not uv pip install


# algae.mat data format

Data are organized in a matlab file as a 1x3 struct array with fields:
- irradiance
- temperature
- pH
- oxygen
- DIC
- nitrate
- phosphate
- chlorophyll_a
- density
- salinity
- PAM0
- PAM8
- PAM16
- comments

Each struct array is dedicated to a particular raceway
Each of the variables (irradiance, pH, etc.) has entries data and (normalized) time, e.g., algae(1).pH.data: [48x1 double]
time_num: [48x1 double]
where
“data” contain the raw measurements
“time_num” is the time baselined to the beginning of the experiments on 2/2/2010 (in units of days).