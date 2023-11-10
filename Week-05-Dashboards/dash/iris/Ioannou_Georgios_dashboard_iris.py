# Ioannou_Georgios
# Copyright © 2023 by Georgios Ioannou
# Filename: Ioannou_Georgios_dashboard_iris.py
##################################################################################
# Import libraries.

import dash
import dash_bootstrap_components as dbc
import seaborn as sns

from dash import dcc, html
from dash.dependencies import Input, Output
from Ioannou_Georgios_dashboard_iris_callbacks import *

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
#################################### FRONTEND ####################################
##################################################################################
# Define the layout of the dashboard.

app.layout = dbc.Container(
    [
        html.H1("Iris Dashboard", className="mt-4"),
        html.H3("Copyright © 2023 by Georgios Ioannou", className="mt-2 mb-5"),
        # Dropdowns to select features for x and y axes.
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("X-Axis Feature"),
                        dcc.Dropdown(
                            id="x-axis-dropdown",
                            options=[
                                {"label": col, "value": col}
                                for col in iris.columns[:-1]
                            ],
                            value=iris.columns[0],
                            multi=False,
                            clearable=False,
                            className="mb-3",
                        ),
                    ],
                    width={"size": 3},
                ),
                dbc.Col(
                    [
                        html.Label("Y-Axis Feature"),
                        dcc.Dropdown(
                            id="y-axis-dropdown",
                            options=[
                                {"label": col, "value": col}
                                for col in iris.columns[:-1]
                            ],
                            value=iris.columns[1],
                            multi=False,
                            clearable=False,
                            className="mb-3",
                        ),
                    ],
                    width={"size": 3},
                ),
                dbc.Col(
                    [
                        html.Label("Z-Axis Feature"),
                        dcc.Dropdown(
                            id="z-axis-dropdown",
                            options=[
                                {"label": col, "value": col}
                                for col in iris.columns[:-1]
                            ],
                            value=iris.columns[2],
                            multi=False,
                            clearable=False,
                            className="mb-3",
                        ),
                    ],
                    width={"size": 3},
                ),
            ]
        ),
        # Switchers for species selection.
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Species:"),
                        dbc.Checklist(
                            id="species-selection",
                            options=[
                                {"label": species, "value": species}
                                for species in all_species
                            ],
                            value=[
                                "setosa",
                                "versicolor",
                                "virginica",
                            ],
                            switch=True,  # Convert to switches.
                            className="mb-3",
                        ),
                    ],
                    width={"size": 12},
                ),
            ]
        ),
        # Tabs for different types of visualizations.
        dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=[
                dcc.Tab(label="1D Plot", value="tab-1"),
                dcc.Tab(label="2D Plot", value="tab-2"),
                dcc.Tab(label="3D Plot", value="tab-3"),
                dcc.Tab(label="Dataset", value="tab-4"),
                dcc.Tab(label="Statistics", value="tab-5"),
            ],
        ),
        # Interactive components.
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            dcc.Slider(
                                id="marker-size-slider",
                                min=1,
                                max=30,
                                step=1,
                                value=15,
                                marks={i: str(i) for i in range(1, 31, 1)},
                                className="m-3",
                            ),
                            style={"display": "none"},
                            id="marker-size-slider-div",
                        ),
                    ],
                    width={"size": 12},
                ),
            ],
            id="interactive-components",
        ),
        # Input for specifying the number of samples to display.
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Number of Samples Per Species:"),
                        dcc.Input(
                            id="num-rows-input",
                            type="number",
                            placeholder="Enter number of samples (up to 50)",
                            value=1,
                            min=1,
                            max=50,
                            className="m-1 mb-3",
                        ),
                        html.Div(
                            id="num-rows-error",
                            className="text-danger",
                        ),
                    ],
                    width={"size": 12},
                ),
            ]
        ),
        # Hidden div to store selected columns for the DataFrame tab.
        html.Div(id="selected-columns-hidden", style={"display": "none"}),
        # Placeholder for Dataset/Statistics tab.
        html.Div(
            [
                html.Label(
                    "Select Columns to Display",
                    className="mt-3 mb-2",
                    style={"font-weight": "bold", "font-size": "18px"},
                ),
                dcc.Dropdown(
                    id="column-selection-dropdown",
                    options=[{"label": col, "value": col} for col in iris.columns],
                    multi=True,
                    value=iris.columns.tolist(),
                    className="mb-3",
                    style={"font-size": "16px"},
                ),
            ],
            id="select-columns-div",
            style={
                "border": "1px solid #ccc",
                "padding": "20px",
                "border-radius": "5px",
            },
        ),
        # Placeholder for visualizations.
        html.Div(id="visualization-output"),
        # Store for selected tab.
        dcc.Store(id="selected-tab", data="tab-1"),
    ]
)


##################################################################################
#################################### BACKEND #####################################
##################################################################################

# Callback to update the visibility of the marker-size-slider.

app.callback(
    Output("marker-size-slider-div", "style"),
    Input("tabs", "value"),
)(update_slider_visibility)

# Callback to update the visibility of the marker-size-slider.

app.callback(
    Output("select-columns-div", "style"),
    Input("tabs", "value"),
)(select_columns_visibility)


# Callback to update the selected columns in the hidden div.

app.callback(
    Output("selected-columns-hidden", "children"),
    Input("column-selection-dropdown", "value"),
)(update_selected_columns)


# Callback to update the visibility of the column-selection-dropdown.

app.callback(
    Output("column-selection-dropdown", "value"),
    Input("tabs", "value"),
)(reset_column_selection)


# Callback to update the selected tab in the dcc.Store.

app.callback(
    Output("selected-tab", "data"),
    Input("tabs", "value"),
)(update_selected_tab)


# Callback to update the visualizations based on user input and display error message.

app.callback(
    [Output("visualization-output", "children"), Output("num-rows-error", "children")],
    Input("x-axis-dropdown", "value"),
    Input("y-axis-dropdown", "value"),
    Input("z-axis-dropdown", "value"),
    Input("tabs", "value"),
    Input("marker-size-slider", "value"),
    Input("num-rows-input", "value"),
    Input("species-selection", "value"),
    Input("selected-columns-hidden", "children"),  # Updated input for selected columns.
)(update_visualizations)

#################################################################################
############################## RUN THE APPLICATION ###############################
##################################################################################

if __name__ == "__main__":
    app.run_server(debug=False, threaded=True)
