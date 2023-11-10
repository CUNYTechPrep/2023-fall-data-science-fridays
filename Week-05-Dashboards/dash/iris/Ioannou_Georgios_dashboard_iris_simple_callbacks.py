# Ioannou_Georgios
# Copyright © 2023 by Georgios Ioannou
# Filename: Ioannou_Georgios_dashboard_iris_simple_callbacks.py
##################################################################################
# Import libraries.

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import seaborn as sns
import json

from dash import dash_table, dcc
from dash.dependencies import Input, Output

##################################################################################

##################################################################################
########################### INITIALIZE THE APPLICATION ###########################
##################################################################################


# Initialize the Dash application with a Bootstrap theme, meta tags, and title.

# EXAMPLE THEMES:
# ALL THEMES CAN BE FOUND HERE: https://bootswatch.com/
#
# dbc.themes.BOOTSTRAP (Default Bootstrap theme)
# dbc.themes.CERULEAN
# dbc.themes.COSMO
# dbc.themes.CYBORG
# dbc.themes.DARKLY
# dbc.themes.FLATLY
# dbc.themes.JOURNAL
# dbc.themes.LITERA
# dbc.themes.LUMEN
# dbc.themes.LUX
# dbc.themes.MATERIA
# dbc.themes.MINTY
# dbc.themes.PULSE
# dbc.themes.SANDSTONE
# dbc.themes.SIMPLEX
# dbc.themes.SLATE
# dbc.themes.SOLAR
# dbc.themes.SPACELAB
# dbc.themes.SUPERHERO
# dbc.themes.UNITED
# dbc.themes.YETI


app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.SLATE,
        "https://use.fontawesome.com/releases/v5.11.2/css/all.css",
        {
            "href": "https://fonts.googleapis.com/icon?family=Material+Icons",
            "rel": "stylesheet",
        },
    ],
    meta_tags=[
        {"name": "charset", "content": "UTF-8"},
        {"name": "description", "content": "Iris Dashboard"},
        {"name": "keywords", "content": "Plotly, Dash, HTML, CSS, Bootstrap"},
        {"name": "author", "content": "Georgios Ioannou"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
        {"property": "og:title", "content": "Iris Dashboard"},
        {"property": "og:type", "content": "website"},
        {"property": "og:image:type", "content": "image/png"},
        {"http-equiv": "X-UA-Compatible", "content": "IE=edge"},
    ],
)

app.title = "Iris Dashboard"
server = app.server
app.config.suppress_callback_exceptions = True

##################################################################################
################################### LOAD DATA ####################################
##################################################################################


# Load the Iris dataset.

iris = sns.load_dataset("iris")


# Add a list of all unique species in the Iris dataset.

all_species = iris["species"].unique()

##################################################################################
############################## CALLBACKS DEFINITIONS #############################
##################################################################################

# Callback to update the visibility of the marker-size-slider.


@app.callback(
    Output("marker-size-slider-div", "style"),
    Input("tabs", "value"),
)
def update_slider_visibility(selected_tab):
    marker_size_slider_style = {}

    if selected_tab in ["tab-1", "tab-2", "tab-3"]:
        marker_size_slider_style = {"display": "block"}
    else:
        marker_size_slider_style = {"display": "none"}

    return marker_size_slider_style


# Callback to update the visibility of the marker-size-slider.


@app.callback(
    Output("select-columns-div", "style"),
    Input("tabs", "value"),
)
def select_columns_visibility(selected_tab):
    select_columns_style = {}

    # Show the menu only for tab-4 (Dataset).

    if selected_tab in ["tab-4", "tab-5"]:
        select_columns_style = {"display": "block"}
    else:
        select_columns_style = {"display": "none"}

    return select_columns_style


# Callback to update the selected columns in the hidden div.


@app.callback(
    Output("selected-columns-hidden", "children"),
    Input("column-selection-dropdown", "value"),
)
def update_selected_columns(selected_columns):
    return json.dumps(selected_columns)


# Callback to update the visibility of the column-selection-dropdown.


@app.callback(
    Output("column-selection-dropdown", "value"),
    Input("tabs", "value"),
)
def reset_column_selection(selected_tab):
    if selected_tab in ["tab-4", "tab-5"]:
        # If switching to the DataFrame tab, reset selected columns based on the hidden div.

        selected_columns_json = app.get_component(
            "selected-columns-hidden"
        ).props.children

        selected_columns = json.loads(selected_columns_json)
        return selected_columns
    else:
        # Otherwise, return the default selection (all columns).

        return iris.columns.tolist()


# Callback to update the selected tab in the dcc.Store.


@app.callback(
    Output("selected-tab", "data"),
    Input("tabs", "value"),
)
def update_selected_tab(selected_tab):
    return selected_tab


# Callback to update the visualizations based on user input and display error message.


@app.callback(
    [Output("visualization-output", "children"), Output("num-rows-error", "children")],
    Input("x-axis-dropdown", "value"),
    Input("y-axis-dropdown", "value"),
    Input("tabs", "value"),
    Input("marker-size-slider", "value"),
    Input("num-rows-input", "value"),
    Input("species-selection", "value"),
    Input("selected-columns-hidden", "children"),  # Updated input for selected columns.
)
def update_visualizations(
    x_axis,
    y_axis,
    selected_tab,
    marker_size,
    num_rows,
    selected_species,
    selected_columns_json,  # Updated input for selected columns.
):
    # Convert the selected columns JSON string back to a list.

    selected_columns = json.loads(selected_columns_json)

    error_message = ""

    # Ensure num_rows is not None and greater than 1.

    if num_rows is None or num_rows < 1:
        num_rows = 1
        error_message = "Please enter a positive number. From 1 to 50 inclusive."

    num_samples_per_species = num_rows

    # Subset of the dataset based on the specified number of samples for each species.
    # Create an empty DataFrame to store the selected samples.

    subset_df = pd.DataFrame()

    for species in selected_species:
        species_df = iris[iris["species"] == species]

        # Check if the requested number of samples is greater than the available population.

        if num_samples_per_species >= len(species_df):
            #  Select all available samples.

            species_sample = species_df
        else:
            species_sample = species_df[:num_samples_per_species]

        subset_df = pd.concat([subset_df, species_sample])

    # Filter the DataFrame based on selected columns.

    subset_df = subset_df[selected_columns]

    # Define a symbol for each species.

    symbol_map = {"setosa": "circle", "versicolor": "square", "virginica": "x"}

    # Define a color for each species.

    species_colors = {
        "setosa": "red",
        "versicolor": "green",
        "virginica": "blue",
    }

    if selected_tab == "tab-1":
        # 2D Plot.

        traces = []

        for species in selected_species:
            species_df = subset_df[subset_df["species"] == species]
            trace = go.Scatter(
                x=species_df[x_axis],
                y=species_df[y_axis],
                mode="markers",
                name=species,
                marker=dict(
                    size=marker_size,
                    color=species_colors[species],
                    symbol=symbol_map[species],
                ),
            )
            traces.append(trace)

        layout = go.Layout(
            title=f"2D Scatter Plot ({x_axis} vs {y_axis}) for {', '.join(selected_species)}",
            xaxis=dict(title=x_axis),
            yaxis=dict(title=y_axis),
        )

        fig = go.Figure(data=traces, layout=layout)
        return dcc.Graph(figure=fig), error_message

    elif selected_tab == "tab-2":
        # Display the DataFrame in a Dash DataTable based on selected columns.

        return (
            dash_table.DataTable(
                id="data-table",
                columns=[{"name": col, "id": col} for col in selected_columns],
                data=subset_df[selected_columns].to_dict("records"),
                style_table={"overflowX": "auto"},
            ),
            error_message,
        )
