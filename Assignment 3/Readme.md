# MongoDB Atlas and MongoDB Community Edition Setup Guide

This guide provides step-by-step instructions to set up MongoDB Atlas and MongoDB Community Edition for running queries using MongoDB Compass as well as two example queries at the end.

## 1. Sign up MongoDB Atlas
To get started with MongoDB Atlas, follow these steps:

1. **Sign up for a MongoDB account:** [Sign up here](https://www.mongodb.com/cloud/atlas/register)
2. **Create a free cluster:** [Follow instructions here](https://www.mongodb.com/docs/guides/atlas/cluster/)
3. **Add a database user:** [Guide for adding a database user](https://www.mongodb.com/docs/guides/atlas/db-user/)
4. **Configure a network connection:** [Instructions for configuring network connection](https://www.mongodb.com/docs/guides/atlas/network-connections/)
5. **Load sample data:** [Guide for loading sample data](https://www.mongodb.com/docs/guides/atlas/sample-data/)
6. **Get connection string:** [Guide for obtaining connection string](https://www.mongodb.com/docs/guides/atlas/connection-string/)

## 2. Install MongoDB Community Edition
To install MongoDB Community Edition, please follow the guide provided below:

- **Installation Guide:** [Install MongoDB Community Edition](https://www.mongodb.com/docs/manual/administration/install-community/)

After installation, use the connection string obtained from MongoDB Atlas to connect to the Atlas cluster.

<img width="1440" alt="Screenshot 2024-03-26 at 9 28 40 PM" src="https://github.com/mcsilva19/cs3980/assets/117865397/573b2534-4f86-4af9-906f-be21da4d793c">

## 3. Run Queries using MongoDB Compass
Once MongoDB Community Edition and MongoDB Atlas are set up, you can run queries using MongoDB Compass. Follow these steps:

- **Embedded MongoDB Shell:** MongoDB Compass provides an embedded MongoDB Shell to run queries. [Learn more here](https://www.mongodb.com/docs/compass/current/embedded-shell/)

## 4. Assignment 

Before writing the queries I moved to the sample data that I wanted to pull from by typing "Use sample_mflix" in mongosh shell terminal.

**Query 1:** Find all movies with runtime greater than 200 minutes in year 1983. The result should include a list of objects sorted by runtime increasing, and each object only has three fields: runtime, title, year. An example result is shown in the following screenshot, where the query is shown in the white text and the results in the red, green, blue text that follows. 
<img width="1440" alt="Screenshot 2024-03-26 at 9 26 37 PM" src="https://github.com/mcsilva19/cs3980/assets/117865397/c113de80-7b3e-4a87-8163-ee40d5a0d671">

<img width="1440" alt="Screenshot 2024-03-26 at 9 26 49 PM" src="https://github.com/mcsilva19/cs3980/assets/117865397/02d545f8-c1d1-4d71-8c4e-71d0b996a578">


**Query 2:** Find all movies after year 2014 with imdb rating greater than 9. An example result is shown in the following screenshot, where the query is shown in the white text and the results in the red, green, blue text that follows. 
<img width="1440" alt="Screenshot 2024-03-26 at 9 27 46 PM" src="https://github.com/mcsilva19/cs3980/assets/117865397/2c3a1075-19c9-416c-91c8-01f952b30e7f">

