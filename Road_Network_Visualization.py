import osmnx as ox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from geopy.geocoders import Nominatim
import pycountry

geolocator = Nominatim(user_agent="road_network_app")

def get_graph():
    selected_country = entry_country.get()
    selected_city = entry_city.get()

    try:
        # Retrieve the road network graph for the specified location
        graph = ox.graph_from_place(f"{selected_city}, {selected_country}", network_type="all")

        # Plot the road network with custom visualization parameters
        fig, ax = ox.plot_graph(ox.project_graph(graph), bgcolor='white', edge_color='#377eb8', node_color='#ff7f00',
                                node_size=30, node_alpha=0.6, edge_linewidth=0.8, edge_alpha=0.6, figsize=(8, 6))

        # Display the plot
        ax.set_title("Road Network Visualization")
        fig.canvas.manager.window.attributes('-topmost', 1)
        fig.canvas.manager.window.attributes('-topmost', 0)
        fig.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the GUI window
window = Tk()
window.title("Road Network Visualization")
window.geometry("400x200")
window.configure(bg='#F0F0F0')  # Set background color

# Create labels and input fields for country and city
label_country = Label(window, text="Country:", bg='#F0F0F0')
label_country.pack()

entry_country = Entry(window)
entry_country.pack()

label_city = Label(window, text="City:", bg='#F0F0F0')
label_city.pack()

entry_city = Entry(window)
entry_city.pack()

# Create visualization button
button_visualize = Button(window, text="Visualize Road Network", command=get_graph, bg='#00AEEF', fg='white')
button_visualize.pack(pady=10)

# Start the GUI event loop
window.mainloop()
