# US Population Table

This simple HTML web page displays a table showing the population of the United States over the years.

## Table of Contents

- [Introduction](#introduction)
- [Code](#Code)
- [Usage](#usage)

## Introduction
The web page fetches population data of the United States from an external API (https://datausa.io/api/data?drilldowns=Nation&measures=Population). Then the data is parsed, sorted, and properly displayed in a table. The population numbers are formatted with commas for better readability.

## Code

### HTML
- 'index.html' is used to structure the web page which includes the title, heading, table, and script inclusion.

### CSS
- 'style.css' is used to help style the table, i included border-collapse, text alignment, and padding for the aesthetic of the web page. 

### Javascript
- 'script.js' is used to fetch the data from the API. In this section the data is also sorted and commas are added in order for the data to be properly showed in the table. 

## Usage

To view the population table:

1. Clone or download the repository.
2. Open the `index.html` file in a web browser.

The table will be populated with the US population data retrieved from the data source. 
