import json
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from metpy.plots import USCOUNTIES
import matplotlib.patches as mpatches

## Open the downloaded geojson file from the website you created the outlook ##
with open('c:\\Users\\tonyi\\Downloads\\data.geojson') as f:
    data = json.load(f)

## Extract the data from the geojson file ##
coordinates = data['features'][0]['geometry']['coordinates'][0]

## Map Stuff ##
color_map = {
    'marginal': 'green',
    'slight': 'yellow',
    # Add more titles and colors as needed
}

# Create a new figure
fig = plt.figure(figsize=(24, 9))

# Create a map
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([-125, -66, 24, 49])
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.STATES)
ax.add_feature(USCOUNTIES.with_scale('5m'), alpha=0.25)
ax.gridlines(draw_labels=True, color='black',linestyle='--', alpha=0.35)

# Loop over the features in the data
for feature in data['features']:
    # Extract the coordinates and title
    coordinates = feature['geometry']['coordinates'][0]
    title = feature['properties']['title']

    # Look up the color for this title
    color = color_map.get(title, 'blue')  # Default to 'blue' if the title is not in the color map

    # Plot the polygon
    ax.plot(*zip(*coordinates), transform=ccrs.PlateCarree(), color=color, linewidth=3)
    ax.fill(*zip(*coordinates), color=color, transform=ccrs.PlateCarree(), alpha=0.3)

legend_patches = []

# Loop over the color_map
for title, color in color_map.items():
    # Create a patch for this title and color
    patch = mpatches.Patch(color=color, label=title)
    
    # Add the patch to the legend_patches list
    legend_patches.append(patch)


plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(handles=legend_patches)
plt.title('METR 4403: Forecast Journal #1 - 1630z Convective Outlook', fontsize=14)
plt.show()