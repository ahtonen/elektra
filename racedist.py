#%%
import pandas as pd
import numpy as np
import os

wpt_stlucia = (14.166, -60.95)

pd.set_option('precision', 3)
os.chdir(os.path.join(os.environ['HOME'], 'src', 'Elektra', 'Positions'))

#%%
def gc_dist_speed(df_boat, df_refboat):
    """ Compute GC distance and mean speed over pos updates. """
    # differences in degrees
    dlat = df_boat['lat'].diff()
    dlon_ = df_boat['lon'].diff()
    # cosine correction
    midlat = df_boat['lat'] + dlat/2
    dlon = np.cos(np.deg2rad(midlat))*dlon_
    # GC distance in nm
    df_boat['distance'] = np.sqrt(np.square(dlat*60) + np.square(dlon*60))
    # speed between updates
    dtime = np.append(np.nan, np.diff(df_boat.index).astype(int)/(3600e9))
    df_boat['speed'] = df_boat['distance'] / dtime

    # distance from St Lucia
    dlat = (df_boat['lat'] - wpt_stlucia[0])
    dlon_ = (df_boat['lon'] - wpt_stlucia[1])
    # cosine correction
    midlat = (df_boat['lat'] + wpt_stlucia[0])/2
    dlon = np.cos(np.deg2rad(midlat))*dlon_
    # GC distance in nm
    df_boat['StLucia'] = np.sqrt(np.square(dlat*60) + np.square(dlon*60))
    # VMG to St. Lucia
    df_boat['VMG_StLucia'] = -df_boat['StLucia'].diff() / dtime
    # distance from us
    dlat = (df_boat['lat'] - df_refboat['lat'])
    dlon_ = (df_boat['lon'] - df_refboat['lon'])
    midlat = (df_boat['lat'] + df_refboat['lat'])/2
    dlon = np.cos(np.deg2rad(midlat))*dlon_

    df_boat['distance_from_us'] = np.sqrt(np.square(dlat*60) + np.square(dlon*60))

    return df_boat

#%% 
# Read all files
report_files = os.listdir()
dfall = pd.DataFrame(columns=["boat", "lat", "lon"])

for file in report_files:
    df = pd.read_csv(file, skiprows=1,
        index_col=3, header=None, sep=';',
        usecols=[1, 2, 3, 4],
        names=["boat", "lat", "lon", "timestamp"],
        parse_dates=True)
    # convert latitudes to float, assume all are N
    df['lat'] = df['lat'].apply(lambda x: float(x[:-1]))
    # convert longitudes to float, assume all are W
    df['lon'] = df['lon'].apply(lambda x: -float(x[:-1]))

    dfall = dfall.append(df)

#%%
def select_boat(dfall, boat_number):
    dfboat = dfall[dfall['boat'] == boat_number].copy()
    dfboat.sort_index(inplace=True)
    # resample to 4h interval and drop lines not containing data
    dfboat = dfboat.resample('4h').mean()
    dfboat.dropna(inplace=True)

    return dfboat

# %%
competitors = {'Vahine': 41, 'BioTrek': 52, 'The Kid': 81, 'Allegra': 23,
    'Hallucine': 98, 'Sisi': 38, 'Interpid': 31, 'Elektra': 150, 
    'Ulisse': 21, 'Fra Diavolo': 50, "Stay Calm": 28, "Umiko": 27,
    "Somewhere in London": 42}

elektra = select_boat(dfall, competitors['Elektra'])
#%%

for boat, number in competitors.items():
    dfboat = select_boat(dfall, number)

    print(f"\n{boat} ({number}) race analytics:")
    dfrace = gc_dist_speed(dfboat, elektra)
    #dfrace.drop(labels='boat', axis=1, inplace=True)
    print(dfrace.iloc[-6:,:])



# %%
