"""
Created on Feb 2024
@author: Agamdeep Chopra
@email: achopra4@uw.edu
@website: https://agamchopra.github.io/
@affiliation: University of Washington, Seattle, USA
@Refs: ChatGPT4
"""
import matplotlib.pyplot as plt
import numpy as np

# Define the individual layers and junctions as provided in the given code snippets

# Anti-reflective coatings (ARC) and window layers
arc_and_window_layers = [
    {"name": "MgF2", "width": 110e-9, "role": "ARC1"},
    {"name": "ZnS", "width": 60e-9, "role": "ARC2"},
    {"name": "AlInP", "width": 30e-9, "role": "window", "Nd": 5e23,
        "Al": 0.53, "electron_mobility": 0.01, "hole_mobility": 7e-4},
]

# GaInP junction layers
gainp_junction_layers = [
    {"name": "GaInP", "width": 120e-9, "role": "Emitter", "Nd": 5e23, "In": 0.49},
    {"name": "GaInP", "width": 800e-9, "role": "Base", "Na": 8e22, "In": 0.49},
    {"name": "AlInP", "width": 100e-9, "role": "BSF", "Na": 5e23,
        "Al": 0.53, "electron_mobility": 0.01, "hole_mobility": 7e-4},
]

# Tunnel junction layer
tunnel_junction_layer = [
    {"name": "GaInP", "width": 40e-9, "role": "TJ", "v_peak": 0.2, "j_peak": 7.5e4,
        "v_valley": 1, "j_valley": 4e4, "prefactor": 5, "j01": 1e-23},
]

# GaAs junction layers (including QWs)
# Note: The QW_list is not explicitly defined in the provided code. Assuming QW_list refers to the QW structure.
qws = [
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "InGaAs", "width": 7e-9, "role": "well", "In": 0.2, "strained": True},
    {"name": "GaAs", "width": 2e-9, "role": "well"},
    {"name": "GaAsP", "width": 10e-9, "role": "barrier", "P": 0.1, "strained": True},
]

gaas_junction_layers = [
    {"name": "GaInP", "width": 10e-9, "role": "Window", "Nd": 5e24, "In": 0.49},
    {"name": "GaAs", "width": 150e-9, "role": "Emitter", "Nd": 1e24},
    # Assuming the QWs are to be included directly
    *qws,
    {"name": "GaAs", "width": 2000e-9, "role": "Base", "Na": 8e22},
    {"name": "GaInP", "width": 200e-9, "role": "BSF", "Na": 5e24, "In": 0.49},
]

# Combine all layers into a single list
all_layers = arc_and_window_layers + gainp_junction_layers + \
    tunnel_junction_layer + gaas_junction_layers

# Use a dictionary to associate unique layer names with specific colors
unique_layer_names = sorted(set(layer['name'] for layer in all_layers))
color_map = {name: plt.cm.Dark2_r(i/len(unique_layer_names))
             for i, name in enumerate(unique_layer_names)}

fig, ax = plt.subplots(figsize=(10, 8), dpi=350)
layer_bottom = 0  # Reset starting position

for layer in reversed(all_layers):  # Reverse the list to flip the order
    # Convert width to nm for better readability
    layer_top = layer_bottom + layer['width'] * 1e9
    ax.fill_between([0, 1], layer_bottom, layer_top, color=color_map[layer['name']],
                    label=f"{layer['name']} ({layer['role']})")
    layer_bottom = layer_top  # Update for the next layer

# To avoid duplicate labels in the legend, we filter out duplicates
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(),
          loc='upper left', bbox_to_anchor=(1, 1))

ax.set_xlim([0, 1])
ax.set_ylim([0, layer_bottom])
ax.set_yticks(np.arange(0, layer_bottom, step=layer_bottom/10))
ax.set_yticklabels(
    [f"{int(ax.get_yticks()[-1] - tick + ax.get_yticks()[1])} nm" for tick in ax.get_yticks()])
ax.set_xticks([])
ax.set_xlabel("Solar Cell Cross-Section")
ax.set_ylabel("Depth (nm)")
ax.set_title("Cross-Sectional View of Solar Cell Layers")

plt.tight_layout()
plt.show()
