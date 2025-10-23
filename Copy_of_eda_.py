{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/BUFONJOKER/BUFON-FIRST--FLUTTER-APP/blob/main/Copy_of_eda_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "a772acf3",
      "metadata": {
        "id": "a772acf3"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "87051eb4",
      "metadata": {
        "id": "87051eb4"
      },
      "outputs": [],
      "source": [
        "df_copy = pd.read_csv(\"dataset/survey.csv\")\n",
        "df = df_copy.copy(deep=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d3333938",
      "metadata": {
        "id": "d3333938",
        "outputId": "d8d51018-01ad-4071-b94d-16c604f2f3a9"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "Index(['Timestamp', 'Age', 'Gender', 'Country', 'state', 'self_employed',\n",
              "       'family_history', 'treatment', 'work_interfere', 'no_employees',\n",
              "       'remote_work', 'tech_company', 'benefits', 'care_options',\n",
              "       'wellness_program', 'seek_help', 'anonymity', 'leave',\n",
              "       'mental_health_consequence', 'phys_health_consequence', 'coworkers',\n",
              "       'supervisor', 'mental_health_interview', 'phys_health_interview',\n",
              "       'mental_vs_physical', 'obs_consequence', 'comments'],\n",
              "      dtype='object')"
            ]
          },
          "execution_count": 183,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "25f67f02",
      "metadata": {
        "id": "25f67f02"
      },
      "outputs": [],
      "source": [
        "# rename columns\n",
        "df.rename(columns={\n",
        "    'Timestamp': 'Timestamp',\n",
        "    'Age': 'Age',\n",
        "    'Gender': 'Gender',\n",
        "    'Country': 'Country',\n",
        "    'state': 'State',\n",
        "    'self_employed': 'Self_Employed',\n",
        "    'family_history': 'Family_History',\n",
        "    'treatment': 'Treatment',\n",
        "    'work_interfere': 'Work_Interfere',\n",
        "    'no_employees': 'No_Employees',\n",
        "    'remote_work': 'Remote_Work',\n",
        "    'tech_company': 'Tech_Company',\n",
        "    'benefits': 'Benefits',\n",
        "    'care_options': 'Care_Options',\n",
        "    'wellness_program': 'Wellness_Program',\n",
        "    'seek_help': 'Seek_Help',\n",
        "    'anonymity': 'Anonymity',\n",
        "    'leave': 'Leave',\n",
        "    'mental_health_consequence': 'Mental_Health_Consequence',\n",
        "    'phys_health_consequence': 'Physical_Health_Consequence',\n",
        "    'coworkers': 'Coworkers',\n",
        "    'supervisor': 'Supervisor',\n",
        "    'mental_health_interview': 'Mental_Health_Interview',\n",
        "    'phys_health_interview': 'Physical_Health_Interview',\n",
        "    'mental_vs_physical': 'Mental_vs_Physical',\n",
        "    'obs_consequence': 'Obs_Consequence',\n",
        "    'comments': 'Comments'\n",
        "}\n",
        ",inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f8e01c57",
      "metadata": {
        "id": "f8e01c57",
        "outputId": "efbb8f25-09af-44cb-f017-ad7d6b5a0b9a"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Timestamp",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Country",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "State",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "Self_Employed",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "Family_History",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Treatment",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Work_Interfere",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "No_Employees",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Remote_Work",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Tech_Company",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Benefits",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Care_Options",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Wellness_Program",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Seek_Help",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Anonymity",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Leave",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Coworkers",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Supervisor",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_vs_Physical",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Obs_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Comments",
                  "rawType": "object",
                  "type": "unknown"
                }
              ],
              "ref": "05f17787-b1e6-40ef-ab17-cef039e72244",
              "rows": [
                [
                  "0",
                  "2014-08-27 11:29:31",
                  "37",
                  "Female",
                  "United States",
                  "IL",
                  null,
                  "No",
                  "Yes",
                  "Often",
                  "6-25",
                  "No",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "No",
                  "Yes",
                  "Yes",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Maybe",
                  "Yes",
                  "No",
                  null
                ],
                [
                  "1",
                  "2014-08-27 11:29:37",
                  "44",
                  "M",
                  "United States",
                  "IN",
                  null,
                  "No",
                  "No",
                  "Rarely",
                  "More than 1000",
                  "No",
                  "No",
                  "Don't know",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No",
                  null
                ],
                [
                  "2",
                  "2014-08-27 11:29:44",
                  "32",
                  "Male",
                  "Canada",
                  null,
                  null,
                  "No",
                  "No",
                  "Rarely",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  null
                ],
                [
                  "3",
                  "2014-08-27 11:29:46",
                  "31",
                  "Male",
                  "United Kingdom",
                  null,
                  null,
                  "Yes",
                  "Yes",
                  "Often",
                  "26-100",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "Somewhat difficult",
                  "Yes",
                  "Yes",
                  "Some of them",
                  "No",
                  "Maybe",
                  "Maybe",
                  "No",
                  "Yes",
                  null
                ],
                [
                  "4",
                  "2014-08-27 11:30:22",
                  "31",
                  "Male",
                  "United States",
                  "TX",
                  null,
                  "No",
                  "No",
                  "Never",
                  "100-500",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No",
                  null
                ]
              ],
              "shape": {
                "columns": 27,
                "rows": 5
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Age</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>Family_History</th>\n",
              "      <th>Treatment</th>\n",
              "      <th>Work_Interfere</th>\n",
              "      <th>No_Employees</th>\n",
              "      <th>...</th>\n",
              "      <th>Leave</th>\n",
              "      <th>Mental_Health_Consequence</th>\n",
              "      <th>Physical_Health_Consequence</th>\n",
              "      <th>Coworkers</th>\n",
              "      <th>Supervisor</th>\n",
              "      <th>Mental_Health_Interview</th>\n",
              "      <th>Physical_Health_Interview</th>\n",
              "      <th>Mental_vs_Physical</th>\n",
              "      <th>Obs_Consequence</th>\n",
              "      <th>Comments</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2014-08-27 11:29:31</td>\n",
              "      <td>37</td>\n",
              "      <td>Female</td>\n",
              "      <td>United States</td>\n",
              "      <td>IL</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>6-25</td>\n",
              "      <td>...</td>\n",
              "      <td>Somewhat easy</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2014-08-27 11:29:37</td>\n",
              "      <td>44</td>\n",
              "      <td>M</td>\n",
              "      <td>United States</td>\n",
              "      <td>IN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Rarely</td>\n",
              "      <td>More than 1000</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2014-08-27 11:29:44</td>\n",
              "      <td>32</td>\n",
              "      <td>Male</td>\n",
              "      <td>Canada</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Rarely</td>\n",
              "      <td>6-25</td>\n",
              "      <td>...</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2014-08-27 11:29:46</td>\n",
              "      <td>31</td>\n",
              "      <td>Male</td>\n",
              "      <td>United Kingdom</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>26-100</td>\n",
              "      <td>...</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>No</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2014-08-27 11:30:22</td>\n",
              "      <td>31</td>\n",
              "      <td>Male</td>\n",
              "      <td>United States</td>\n",
              "      <td>TX</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Never</td>\n",
              "      <td>100-500</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 27 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "             Timestamp  Age  Gender         Country State Self_Employed  \\\n",
              "0  2014-08-27 11:29:31   37  Female   United States    IL           NaN   \n",
              "1  2014-08-27 11:29:37   44       M   United States    IN           NaN   \n",
              "2  2014-08-27 11:29:44   32    Male          Canada   NaN           NaN   \n",
              "3  2014-08-27 11:29:46   31    Male  United Kingdom   NaN           NaN   \n",
              "4  2014-08-27 11:30:22   31    Male   United States    TX           NaN   \n",
              "\n",
              "  Family_History Treatment Work_Interfere    No_Employees  ...  \\\n",
              "0             No       Yes          Often            6-25  ...   \n",
              "1             No        No         Rarely  More than 1000  ...   \n",
              "2             No        No         Rarely            6-25  ...   \n",
              "3            Yes       Yes          Often          26-100  ...   \n",
              "4             No        No          Never         100-500  ...   \n",
              "\n",
              "                Leave Mental_Health_Consequence Physical_Health_Consequence  \\\n",
              "0       Somewhat easy                        No                          No   \n",
              "1          Don't know                     Maybe                          No   \n",
              "2  Somewhat difficult                        No                          No   \n",
              "3  Somewhat difficult                       Yes                         Yes   \n",
              "4          Don't know                        No                          No   \n",
              "\n",
              "      Coworkers Supervisor Mental_Health_Interview Physical_Health_Interview  \\\n",
              "0  Some of them        Yes                      No                     Maybe   \n",
              "1            No         No                      No                        No   \n",
              "2           Yes        Yes                     Yes                       Yes   \n",
              "3  Some of them         No                   Maybe                     Maybe   \n",
              "4  Some of them        Yes                     Yes                       Yes   \n",
              "\n",
              "  Mental_vs_Physical Obs_Consequence Comments  \n",
              "0                Yes              No      NaN  \n",
              "1         Don't know              No      NaN  \n",
              "2                 No              No      NaN  \n",
              "3                 No             Yes      NaN  \n",
              "4         Don't know              No      NaN  \n",
              "\n",
              "[5 rows x 27 columns]"
            ]
          },
          "execution_count": 185,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.head(5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8d1cddbd",
      "metadata": {
        "id": "8d1cddbd",
        "outputId": "954afc13-10e6-4011-f719-350d2a20b179"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Timestamp",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Country",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "State",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "Self_Employed",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Family_History",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Treatment",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Work_Interfere",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "No_Employees",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Remote_Work",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Tech_Company",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Benefits",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Care_Options",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Wellness_Program",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Seek_Help",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Anonymity",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Leave",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Coworkers",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Supervisor",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_vs_Physical",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Obs_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Comments",
                  "rawType": "object",
                  "type": "unknown"
                }
              ],
              "ref": "0ccd6795-60ce-428a-9d56-1535816ce898",
              "rows": [
                [
                  "1254",
                  "2015-09-12 11:17:21",
                  "26",
                  "male",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "Yes",
                  null,
                  "26-100",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Some of them",
                  "No",
                  "No",
                  "Don't know",
                  "No",
                  null
                ],
                [
                  "1255",
                  "2015-09-26 01:07:35",
                  "32",
                  "Male",
                  "United States",
                  "IL",
                  "No",
                  "Yes",
                  "Yes",
                  "Often",
                  "26-100",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "Somewhat difficult",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "No",
                  null
                ],
                [
                  "1256",
                  "2015-11-07 12:36:58",
                  "34",
                  "male",
                  "United States",
                  "CA",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "More than 1000",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  null
                ],
                [
                  "1257",
                  "2015-11-30 21:25:06",
                  "46",
                  "f",
                  "United States",
                  "NC",
                  "No",
                  "No",
                  "No",
                  null,
                  "100-500",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  null
                ],
                [
                  "1258",
                  "2016-02-01 23:04:31",
                  "25",
                  "Male",
                  "United States",
                  "IL",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "Don't know",
                  "Maybe",
                  "No",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No",
                  null
                ]
              ],
              "shape": {
                "columns": 27,
                "rows": 5
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Timestamp</th>\n",
              "      <th>Age</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>Family_History</th>\n",
              "      <th>Treatment</th>\n",
              "      <th>Work_Interfere</th>\n",
              "      <th>No_Employees</th>\n",
              "      <th>...</th>\n",
              "      <th>Leave</th>\n",
              "      <th>Mental_Health_Consequence</th>\n",
              "      <th>Physical_Health_Consequence</th>\n",
              "      <th>Coworkers</th>\n",
              "      <th>Supervisor</th>\n",
              "      <th>Mental_Health_Interview</th>\n",
              "      <th>Physical_Health_Interview</th>\n",
              "      <th>Mental_vs_Physical</th>\n",
              "      <th>Obs_Consequence</th>\n",
              "      <th>Comments</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1254</th>\n",
              "      <td>2015-09-12 11:17:21</td>\n",
              "      <td>26</td>\n",
              "      <td>male</td>\n",
              "      <td>United Kingdom</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>NaN</td>\n",
              "      <td>26-100</td>\n",
              "      <td>...</td>\n",
              "      <td>Somewhat easy</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1255</th>\n",
              "      <td>2015-09-26 01:07:35</td>\n",
              "      <td>32</td>\n",
              "      <td>Male</td>\n",
              "      <td>United States</td>\n",
              "      <td>IL</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>26-100</td>\n",
              "      <td>...</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1256</th>\n",
              "      <td>2015-11-07 12:36:58</td>\n",
              "      <td>34</td>\n",
              "      <td>male</td>\n",
              "      <td>United States</td>\n",
              "      <td>CA</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Sometimes</td>\n",
              "      <td>More than 1000</td>\n",
              "      <td>...</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1257</th>\n",
              "      <td>2015-11-30 21:25:06</td>\n",
              "      <td>46</td>\n",
              "      <td>f</td>\n",
              "      <td>United States</td>\n",
              "      <td>NC</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "      <td>100-500</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1258</th>\n",
              "      <td>2016-02-01 23:04:31</td>\n",
              "      <td>25</td>\n",
              "      <td>Male</td>\n",
              "      <td>United States</td>\n",
              "      <td>IL</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Sometimes</td>\n",
              "      <td>26-100</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 27 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                Timestamp  Age Gender         Country State Self_Employed  \\\n",
              "1254  2015-09-12 11:17:21   26   male  United Kingdom   NaN            No   \n",
              "1255  2015-09-26 01:07:35   32   Male   United States    IL            No   \n",
              "1256  2015-11-07 12:36:58   34   male   United States    CA            No   \n",
              "1257  2015-11-30 21:25:06   46      f   United States    NC            No   \n",
              "1258  2016-02-01 23:04:31   25   Male   United States    IL            No   \n",
              "\n",
              "     Family_History Treatment Work_Interfere    No_Employees  ...  \\\n",
              "1254             No       Yes            NaN          26-100  ...   \n",
              "1255            Yes       Yes          Often          26-100  ...   \n",
              "1256            Yes       Yes      Sometimes  More than 1000  ...   \n",
              "1257             No        No            NaN         100-500  ...   \n",
              "1258            Yes       Yes      Sometimes          26-100  ...   \n",
              "\n",
              "                   Leave Mental_Health_Consequence  \\\n",
              "1254       Somewhat easy                        No   \n",
              "1255  Somewhat difficult                        No   \n",
              "1256  Somewhat difficult                       Yes   \n",
              "1257          Don't know                       Yes   \n",
              "1258          Don't know                     Maybe   \n",
              "\n",
              "     Physical_Health_Consequence     Coworkers    Supervisor  \\\n",
              "1254                          No  Some of them  Some of them   \n",
              "1255                          No  Some of them           Yes   \n",
              "1256                         Yes            No            No   \n",
              "1257                          No            No            No   \n",
              "1258                          No  Some of them            No   \n",
              "\n",
              "     Mental_Health_Interview Physical_Health_Interview Mental_vs_Physical  \\\n",
              "1254                      No                        No         Don't know   \n",
              "1255                      No                        No                Yes   \n",
              "1256                      No                        No                 No   \n",
              "1257                      No                        No                 No   \n",
              "1258                      No                        No         Don't know   \n",
              "\n",
              "     Obs_Consequence Comments  \n",
              "1254              No      NaN  \n",
              "1255              No      NaN  \n",
              "1256              No      NaN  \n",
              "1257              No      NaN  \n",
              "1258              No      NaN  \n",
              "\n",
              "[5 rows x 27 columns]"
            ]
          },
          "execution_count": 186,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.tail(5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "7b6067a2",
      "metadata": {
        "id": "7b6067a2",
        "outputId": "ec2d4548-70db-491a-b27b-24b50311b4b1"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(1259, 27)"
            ]
          },
          "execution_count": 187,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8c109a53",
      "metadata": {
        "id": "8c109a53",
        "outputId": "7220dda3-cfa6-40c6-a61a-144404b290b3"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "Index(['Timestamp', 'Age', 'Gender', 'Country', 'State', 'Self_Employed',\n",
              "       'Family_History', 'Treatment', 'Work_Interfere', 'No_Employees',\n",
              "       'Remote_Work', 'Tech_Company', 'Benefits', 'Care_Options',\n",
              "       'Wellness_Program', 'Seek_Help', 'Anonymity', 'Leave',\n",
              "       'Mental_Health_Consequence', 'Physical_Health_Consequence', 'Coworkers',\n",
              "       'Supervisor', 'Mental_Health_Interview', 'Physical_Health_Interview',\n",
              "       'Mental_vs_Physical', 'Obs_Consequence', 'Comments'],\n",
              "      dtype='object')"
            ]
          },
          "execution_count": 188,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8754ef96",
      "metadata": {
        "id": "8754ef96",
        "outputId": "2f5771a1-e69e-4207-87e2-3e1c5308bab1"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1259 entries, 0 to 1258\n",
            "Data columns (total 27 columns):\n",
            " #   Column                       Non-Null Count  Dtype \n",
            "---  ------                       --------------  ----- \n",
            " 0   Timestamp                    1259 non-null   object\n",
            " 1   Age                          1259 non-null   int64 \n",
            " 2   Gender                       1259 non-null   object\n",
            " 3   Country                      1259 non-null   object\n",
            " 4   State                        744 non-null    object\n",
            " 5   Self_Employed                1241 non-null   object\n",
            " 6   Family_History               1259 non-null   object\n",
            " 7   Treatment                    1259 non-null   object\n",
            " 8   Work_Interfere               995 non-null    object\n",
            " 9   No_Employees                 1259 non-null   object\n",
            " 10  Remote_Work                  1259 non-null   object\n",
            " 11  Tech_Company                 1259 non-null   object\n",
            " 12  Benefits                     1259 non-null   object\n",
            " 13  Care_Options                 1259 non-null   object\n",
            " 14  Wellness_Program             1259 non-null   object\n",
            " 15  Seek_Help                    1259 non-null   object\n",
            " 16  Anonymity                    1259 non-null   object\n",
            " 17  Leave                        1259 non-null   object\n",
            " 18  Mental_Health_Consequence    1259 non-null   object\n",
            " 19  Physical_Health_Consequence  1259 non-null   object\n",
            " 20  Coworkers                    1259 non-null   object\n",
            " 21  Supervisor                   1259 non-null   object\n",
            " 22  Mental_Health_Interview      1259 non-null   object\n",
            " 23  Physical_Health_Interview    1259 non-null   object\n",
            " 24  Mental_vs_Physical           1259 non-null   object\n",
            " 25  Obs_Consequence              1259 non-null   object\n",
            " 26  Comments                     164 non-null    object\n",
            "dtypes: int64(1), object(26)\n",
            "memory usage: 265.7+ KB\n"
          ]
        }
      ],
      "source": [
        "df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fbd95a16",
      "metadata": {
        "id": "fbd95a16",
        "outputId": "6963df8a-5ff9-40fb-f0ac-2a3ebb5f627b"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Age",
                  "rawType": "float64",
                  "type": "float"
                }
              ],
              "ref": "8e134f0d-0a6a-4795-a99c-0bc6d5208688",
              "rows": [
                [
                  "count",
                  "1259.0"
                ],
                [
                  "mean",
                  "79428148.31135821"
                ],
                [
                  "std",
                  "2818299442.9819684"
                ],
                [
                  "min",
                  "-1726.0"
                ],
                [
                  "25%",
                  "27.0"
                ],
                [
                  "50%",
                  "31.0"
                ],
                [
                  "75%",
                  "36.0"
                ],
                [
                  "max",
                  "99999999999.0"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 8
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1.259000e+03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>7.942815e+07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>2.818299e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>-1.726000e+03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2.700000e+01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>3.100000e+01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>3.600000e+01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1.000000e+11</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                Age\n",
              "count  1.259000e+03\n",
              "mean   7.942815e+07\n",
              "std    2.818299e+09\n",
              "min   -1.726000e+03\n",
              "25%    2.700000e+01\n",
              "50%    3.100000e+01\n",
              "75%    3.600000e+01\n",
              "max    1.000000e+11"
            ]
          },
          "execution_count": 190,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "415d880a",
      "metadata": {
        "id": "415d880a",
        "outputId": "a012bae2-79a6-45ca-b95c-e471a5e071e2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Timestamp                         0\n",
            "Age                               0\n",
            "Gender                            0\n",
            "Country                           0\n",
            "State                           515\n",
            "Self_Employed                    18\n",
            "Family_History                    0\n",
            "Treatment                         0\n",
            "Work_Interfere                  264\n",
            "No_Employees                      0\n",
            "Remote_Work                       0\n",
            "Tech_Company                      0\n",
            "Benefits                          0\n",
            "Care_Options                      0\n",
            "Wellness_Program                  0\n",
            "Seek_Help                         0\n",
            "Anonymity                         0\n",
            "Leave                             0\n",
            "Mental_Health_Consequence         0\n",
            "Physical_Health_Consequence       0\n",
            "Coworkers                         0\n",
            "Supervisor                        0\n",
            "Mental_Health_Interview           0\n",
            "Physical_Health_Interview         0\n",
            "Mental_vs_Physical                0\n",
            "Obs_Consequence                   0\n",
            "Comments                       1095\n",
            "dtype: int64\n"
          ]
        }
      ],
      "source": [
        "print(df.isnull().sum())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "af987b3a",
      "metadata": {
        "id": "af987b3a",
        "outputId": "4a660499-c665-464f-fcd8-40c5a33409da"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "np.int64(0)"
            ]
          },
          "execution_count": 192,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.duplicated().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "603a82ca",
      "metadata": {
        "id": "603a82ca",
        "outputId": "0783b226-fd7a-4677-816f-f48b122fcbdf"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "0",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "b720a6a9-2b9b-4517-8257-18af30f6c952",
              "rows": [
                [
                  "Timestamp",
                  "1259"
                ],
                [
                  "Age",
                  "1259"
                ],
                [
                  "Gender",
                  "1259"
                ],
                [
                  "Country",
                  "1259"
                ],
                [
                  "State",
                  "744"
                ],
                [
                  "Self_Employed",
                  "1241"
                ],
                [
                  "Family_History",
                  "1259"
                ],
                [
                  "Treatment",
                  "1259"
                ],
                [
                  "Work_Interfere",
                  "995"
                ],
                [
                  "No_Employees",
                  "1259"
                ],
                [
                  "Remote_Work",
                  "1259"
                ],
                [
                  "Tech_Company",
                  "1259"
                ],
                [
                  "Benefits",
                  "1259"
                ],
                [
                  "Care_Options",
                  "1259"
                ],
                [
                  "Wellness_Program",
                  "1259"
                ],
                [
                  "Seek_Help",
                  "1259"
                ],
                [
                  "Anonymity",
                  "1259"
                ],
                [
                  "Leave",
                  "1259"
                ],
                [
                  "Mental_Health_Consequence",
                  "1259"
                ],
                [
                  "Physical_Health_Consequence",
                  "1259"
                ],
                [
                  "Coworkers",
                  "1259"
                ],
                [
                  "Supervisor",
                  "1259"
                ],
                [
                  "Mental_Health_Interview",
                  "1259"
                ],
                [
                  "Physical_Health_Interview",
                  "1259"
                ],
                [
                  "Mental_vs_Physical",
                  "1259"
                ],
                [
                  "Obs_Consequence",
                  "1259"
                ],
                [
                  "Comments",
                  "164"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 27
              }
            },
            "text/plain": [
              "Timestamp                      1259\n",
              "Age                            1259\n",
              "Gender                         1259\n",
              "Country                        1259\n",
              "State                           744\n",
              "Self_Employed                  1241\n",
              "Family_History                 1259\n",
              "Treatment                      1259\n",
              "Work_Interfere                  995\n",
              "No_Employees                   1259\n",
              "Remote_Work                    1259\n",
              "Tech_Company                   1259\n",
              "Benefits                       1259\n",
              "Care_Options                   1259\n",
              "Wellness_Program               1259\n",
              "Seek_Help                      1259\n",
              "Anonymity                      1259\n",
              "Leave                          1259\n",
              "Mental_Health_Consequence      1259\n",
              "Physical_Health_Consequence    1259\n",
              "Coworkers                      1259\n",
              "Supervisor                     1259\n",
              "Mental_Health_Interview        1259\n",
              "Physical_Health_Interview      1259\n",
              "Mental_vs_Physical             1259\n",
              "Obs_Consequence                1259\n",
              "Comments                        164\n",
              "dtype: int64"
            ]
          },
          "execution_count": 193,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.count()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6b58b030",
      "metadata": {
        "id": "6b58b030",
        "outputId": "2b7375ca-31d8-4dbf-d2bb-84b522c24ffb"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "np.int64(1095)"
            ]
          },
          "execution_count": 194,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# drop comments column due to less values\n",
        "df['Comments'].isnull().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c9314d4a",
      "metadata": {
        "id": "c9314d4a"
      },
      "outputs": [],
      "source": [
        "df.drop(labels='Comments', axis=1, inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "a97a5108",
      "metadata": {
        "id": "a97a5108",
        "outputId": "e8e761f1-47f3-4891-cfc6-401b5bedb6da"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "Index(['Timestamp', 'Age', 'Gender', 'Country', 'State', 'Self_Employed',\n",
              "       'Family_History', 'Treatment', 'Work_Interfere', 'No_Employees',\n",
              "       'Remote_Work', 'Tech_Company', 'Benefits', 'Care_Options',\n",
              "       'Wellness_Program', 'Seek_Help', 'Anonymity', 'Leave',\n",
              "       'Mental_Health_Consequence', 'Physical_Health_Consequence', 'Coworkers',\n",
              "       'Supervisor', 'Mental_Health_Interview', 'Physical_Health_Interview',\n",
              "       'Mental_vs_Physical', 'Obs_Consequence'],\n",
              "      dtype='object')"
            ]
          },
          "execution_count": 196,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "bbe22857",
      "metadata": {
        "id": "bbe22857"
      },
      "outputs": [],
      "source": [
        "# drop timestamp column\n",
        "df.drop(labels='Timestamp',axis=1, inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "4ce8797c",
      "metadata": {
        "id": "4ce8797c",
        "outputId": "8c96ecab-1a29-4b89-c855-55aaba4b821d"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "0",
                  "rawType": "object",
                  "type": "string"
                }
              ],
              "ref": "bbdd0346-0b2b-426a-b776-ba9250677b27",
              "rows": [
                [
                  "0",
                  "United States"
                ],
                [
                  "1",
                  "Canada"
                ],
                [
                  "2",
                  "United Kingdom"
                ],
                [
                  "3",
                  "Bulgaria"
                ],
                [
                  "4",
                  "France"
                ],
                [
                  "5",
                  "Portugal"
                ],
                [
                  "6",
                  "Netherlands"
                ],
                [
                  "7",
                  "Switzerland"
                ],
                [
                  "8",
                  "Poland"
                ],
                [
                  "9",
                  "Australia"
                ],
                [
                  "10",
                  "Germany"
                ],
                [
                  "11",
                  "Russia"
                ],
                [
                  "12",
                  "Mexico"
                ],
                [
                  "13",
                  "Brazil"
                ],
                [
                  "14",
                  "Slovenia"
                ],
                [
                  "15",
                  "Costa Rica"
                ],
                [
                  "16",
                  "Austria"
                ],
                [
                  "17",
                  "Ireland"
                ],
                [
                  "18",
                  "India"
                ],
                [
                  "19",
                  "South Africa"
                ],
                [
                  "20",
                  "Italy"
                ],
                [
                  "21",
                  "Sweden"
                ],
                [
                  "22",
                  "Colombia"
                ],
                [
                  "23",
                  "Latvia"
                ],
                [
                  "24",
                  "Romania"
                ],
                [
                  "25",
                  "Belgium"
                ],
                [
                  "26",
                  "New Zealand"
                ],
                [
                  "27",
                  "Zimbabwe"
                ],
                [
                  "28",
                  "Spain"
                ],
                [
                  "29",
                  "Finland"
                ],
                [
                  "30",
                  "Uruguay"
                ],
                [
                  "31",
                  "Israel"
                ],
                [
                  "32",
                  "Bosnia and Herzegovina"
                ],
                [
                  "33",
                  "Hungary"
                ],
                [
                  "34",
                  "Singapore"
                ],
                [
                  "35",
                  "Japan"
                ],
                [
                  "36",
                  "Nigeria"
                ],
                [
                  "37",
                  "Croatia"
                ],
                [
                  "38",
                  "Norway"
                ],
                [
                  "39",
                  "Thailand"
                ],
                [
                  "40",
                  "Denmark"
                ],
                [
                  "41",
                  "Bahamas, The"
                ],
                [
                  "42",
                  "Greece"
                ],
                [
                  "43",
                  "Moldova"
                ],
                [
                  "44",
                  "Georgia"
                ],
                [
                  "45",
                  "China"
                ],
                [
                  "46",
                  "Czech Republic"
                ],
                [
                  "47",
                  "Philippines"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 48
              }
            },
            "text/plain": [
              "array(['United States', 'Canada', 'United Kingdom', 'Bulgaria', 'France',\n",
              "       'Portugal', 'Netherlands', 'Switzerland', 'Poland', 'Australia',\n",
              "       'Germany', 'Russia', 'Mexico', 'Brazil', 'Slovenia', 'Costa Rica',\n",
              "       'Austria', 'Ireland', 'India', 'South Africa', 'Italy', 'Sweden',\n",
              "       'Colombia', 'Latvia', 'Romania', 'Belgium', 'New Zealand',\n",
              "       'Zimbabwe', 'Spain', 'Finland', 'Uruguay', 'Israel',\n",
              "       'Bosnia and Herzegovina', 'Hungary', 'Singapore', 'Japan',\n",
              "       'Nigeria', 'Croatia', 'Norway', 'Thailand', 'Denmark',\n",
              "       'Bahamas, The', 'Greece', 'Moldova', 'Georgia', 'China',\n",
              "       'Czech Republic', 'Philippines'], dtype=object)"
            ]
          },
          "execution_count": 198,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['Country'].unique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e339a446",
      "metadata": {
        "id": "e339a446",
        "outputId": "1db78a9f-b7b4-41a5-bbcf-d830476d4a29"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "a124d76f-1b96-4c10-8a3f-1b5402c17ff0",
              "rows": [
                [
                  "0",
                  "37"
                ],
                [
                  "1",
                  "44"
                ],
                [
                  "2",
                  "32"
                ],
                [
                  "3",
                  "31"
                ],
                [
                  "4",
                  "31"
                ],
                [
                  "5",
                  "33"
                ],
                [
                  "6",
                  "35"
                ],
                [
                  "7",
                  "39"
                ],
                [
                  "8",
                  "42"
                ],
                [
                  "9",
                  "23"
                ],
                [
                  "10",
                  "31"
                ],
                [
                  "11",
                  "29"
                ],
                [
                  "12",
                  "42"
                ],
                [
                  "13",
                  "36"
                ],
                [
                  "14",
                  "27"
                ],
                [
                  "15",
                  "29"
                ],
                [
                  "16",
                  "23"
                ],
                [
                  "17",
                  "32"
                ],
                [
                  "18",
                  "46"
                ],
                [
                  "19",
                  "36"
                ],
                [
                  "20",
                  "29"
                ],
                [
                  "21",
                  "31"
                ],
                [
                  "22",
                  "46"
                ],
                [
                  "23",
                  "41"
                ],
                [
                  "24",
                  "33"
                ],
                [
                  "25",
                  "35"
                ],
                [
                  "26",
                  "33"
                ],
                [
                  "27",
                  "35"
                ],
                [
                  "28",
                  "34"
                ],
                [
                  "29",
                  "37"
                ],
                [
                  "30",
                  "32"
                ],
                [
                  "31",
                  "31"
                ],
                [
                  "32",
                  "30"
                ],
                [
                  "33",
                  "42"
                ],
                [
                  "34",
                  "40"
                ],
                [
                  "35",
                  "27"
                ],
                [
                  "36",
                  "29"
                ],
                [
                  "37",
                  "38"
                ],
                [
                  "38",
                  "50"
                ],
                [
                  "39",
                  "35"
                ],
                [
                  "40",
                  "24"
                ],
                [
                  "41",
                  "35"
                ],
                [
                  "42",
                  "27"
                ],
                [
                  "43",
                  "18"
                ],
                [
                  "44",
                  "30"
                ],
                [
                  "45",
                  "38"
                ],
                [
                  "46",
                  "28"
                ],
                [
                  "47",
                  "34"
                ],
                [
                  "48",
                  "26"
                ],
                [
                  "49",
                  "30"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 1259
              }
            },
            "text/plain": [
              "0       37\n",
              "1       44\n",
              "2       32\n",
              "3       31\n",
              "4       31\n",
              "        ..\n",
              "1254    26\n",
              "1255    32\n",
              "1256    34\n",
              "1257    46\n",
              "1258    25\n",
              "Name: Age, Length: 1259, dtype: int64"
            ]
          },
          "execution_count": 199,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['Age']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "82e08110",
      "metadata": {
        "id": "82e08110",
        "outputId": "645823c6-e9bd-4061-cb2c-f8de30f07e3f"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "0",
                  "rawType": "bool",
                  "type": "boolean"
                }
              ],
              "ref": "96439240-11c8-4434-9ecc-3fa050759ffc",
              "rows": [
                [
                  "0",
                  "False"
                ],
                [
                  "1",
                  "False"
                ],
                [
                  "2",
                  "False"
                ],
                [
                  "3",
                  "False"
                ],
                [
                  "4",
                  "False"
                ],
                [
                  "5",
                  "False"
                ],
                [
                  "6",
                  "False"
                ],
                [
                  "7",
                  "False"
                ],
                [
                  "8",
                  "False"
                ],
                [
                  "9",
                  "False"
                ],
                [
                  "10",
                  "False"
                ],
                [
                  "11",
                  "False"
                ],
                [
                  "12",
                  "False"
                ],
                [
                  "13",
                  "False"
                ],
                [
                  "14",
                  "False"
                ],
                [
                  "15",
                  "False"
                ],
                [
                  "16",
                  "False"
                ],
                [
                  "17",
                  "False"
                ],
                [
                  "18",
                  "False"
                ],
                [
                  "19",
                  "False"
                ],
                [
                  "20",
                  "False"
                ],
                [
                  "21",
                  "False"
                ],
                [
                  "22",
                  "False"
                ],
                [
                  "23",
                  "False"
                ],
                [
                  "24",
                  "False"
                ],
                [
                  "25",
                  "False"
                ],
                [
                  "26",
                  "False"
                ],
                [
                  "27",
                  "False"
                ],
                [
                  "28",
                  "False"
                ],
                [
                  "29",
                  "False"
                ],
                [
                  "30",
                  "False"
                ],
                [
                  "31",
                  "False"
                ],
                [
                  "32",
                  "False"
                ],
                [
                  "33",
                  "False"
                ],
                [
                  "34",
                  "False"
                ],
                [
                  "35",
                  "False"
                ],
                [
                  "36",
                  "False"
                ],
                [
                  "37",
                  "False"
                ],
                [
                  "38",
                  "False"
                ],
                [
                  "39",
                  "False"
                ],
                [
                  "40",
                  "False"
                ],
                [
                  "41",
                  "False"
                ],
                [
                  "42",
                  "False"
                ],
                [
                  "43",
                  "False"
                ],
                [
                  "44",
                  "False"
                ],
                [
                  "45",
                  "False"
                ],
                [
                  "46",
                  "False"
                ],
                [
                  "47",
                  "False"
                ],
                [
                  "48",
                  "False"
                ],
                [
                  "49",
                  "False"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 1259
              }
            },
            "text/plain": [
              "0       False\n",
              "1       False\n",
              "2       False\n",
              "3       False\n",
              "4       False\n",
              "        ...  \n",
              "1254    False\n",
              "1255    False\n",
              "1256    False\n",
              "1257    False\n",
              "1258    False\n",
              "Length: 1259, dtype: bool"
            ]
          },
          "execution_count": 200,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.duplicated()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "55ff03db",
      "metadata": {
        "id": "55ff03db"
      },
      "outputs": [],
      "source": [
        "# remove duplicate rows\n",
        "df.drop_duplicates(inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "4de69829",
      "metadata": {
        "id": "4de69829",
        "outputId": "d1c8a883-4a4f-4363-a8fc-8cd089e56029"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "0",
                  "rawType": "bool",
                  "type": "boolean"
                }
              ],
              "ref": "399acd34-b1b9-4dea-a7ec-dd6e1a22c6c7",
              "rows": [
                [
                  "0",
                  "False"
                ],
                [
                  "1",
                  "False"
                ],
                [
                  "2",
                  "False"
                ],
                [
                  "3",
                  "False"
                ],
                [
                  "4",
                  "False"
                ],
                [
                  "5",
                  "False"
                ],
                [
                  "6",
                  "False"
                ],
                [
                  "7",
                  "False"
                ],
                [
                  "8",
                  "False"
                ],
                [
                  "9",
                  "False"
                ],
                [
                  "10",
                  "False"
                ],
                [
                  "11",
                  "False"
                ],
                [
                  "12",
                  "False"
                ],
                [
                  "13",
                  "False"
                ],
                [
                  "14",
                  "False"
                ],
                [
                  "15",
                  "False"
                ],
                [
                  "16",
                  "False"
                ],
                [
                  "17",
                  "False"
                ],
                [
                  "18",
                  "False"
                ],
                [
                  "19",
                  "False"
                ],
                [
                  "20",
                  "False"
                ],
                [
                  "21",
                  "False"
                ],
                [
                  "22",
                  "False"
                ],
                [
                  "23",
                  "False"
                ],
                [
                  "24",
                  "False"
                ],
                [
                  "25",
                  "False"
                ],
                [
                  "26",
                  "False"
                ],
                [
                  "27",
                  "False"
                ],
                [
                  "28",
                  "False"
                ],
                [
                  "29",
                  "False"
                ],
                [
                  "30",
                  "False"
                ],
                [
                  "31",
                  "False"
                ],
                [
                  "32",
                  "False"
                ],
                [
                  "33",
                  "False"
                ],
                [
                  "34",
                  "False"
                ],
                [
                  "35",
                  "False"
                ],
                [
                  "36",
                  "False"
                ],
                [
                  "37",
                  "False"
                ],
                [
                  "38",
                  "False"
                ],
                [
                  "39",
                  "False"
                ],
                [
                  "40",
                  "False"
                ],
                [
                  "41",
                  "False"
                ],
                [
                  "42",
                  "False"
                ],
                [
                  "43",
                  "False"
                ],
                [
                  "44",
                  "False"
                ],
                [
                  "45",
                  "False"
                ],
                [
                  "46",
                  "False"
                ],
                [
                  "47",
                  "False"
                ],
                [
                  "48",
                  "False"
                ],
                [
                  "49",
                  "False"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 1255
              }
            },
            "text/plain": [
              "0       False\n",
              "1       False\n",
              "2       False\n",
              "3       False\n",
              "4       False\n",
              "        ...  \n",
              "1254    False\n",
              "1255    False\n",
              "1256    False\n",
              "1257    False\n",
              "1258    False\n",
              "Length: 1255, dtype: bool"
            ]
          },
          "execution_count": 202,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.duplicated()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1006367e",
      "metadata": {
        "id": "1006367e",
        "outputId": "cd484f59-4523-40ef-dd50-1f60495d2221"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "count",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "0c75321a-0afd-4f82-a2b5-07f4b04ea4e6",
              "rows": [
                [
                  "29",
                  "85"
                ],
                [
                  "32",
                  "81"
                ],
                [
                  "26",
                  "75"
                ],
                [
                  "27",
                  "70"
                ],
                [
                  "33",
                  "70"
                ],
                [
                  "28",
                  "67"
                ],
                [
                  "31",
                  "67"
                ],
                [
                  "34",
                  "65"
                ],
                [
                  "30",
                  "63"
                ],
                [
                  "25",
                  "61"
                ],
                [
                  "35",
                  "54"
                ],
                [
                  "23",
                  "51"
                ],
                [
                  "24",
                  "46"
                ],
                [
                  "37",
                  "43"
                ],
                [
                  "38",
                  "39"
                ],
                [
                  "36",
                  "37"
                ],
                [
                  "39",
                  "33"
                ],
                [
                  "40",
                  "33"
                ],
                [
                  "43",
                  "28"
                ],
                [
                  "41",
                  "21"
                ],
                [
                  "22",
                  "21"
                ],
                [
                  "42",
                  "20"
                ],
                [
                  "21",
                  "16"
                ],
                [
                  "45",
                  "12"
                ],
                [
                  "46",
                  "12"
                ],
                [
                  "44",
                  "11"
                ],
                [
                  "19",
                  "9"
                ],
                [
                  "18",
                  "7"
                ],
                [
                  "50",
                  "6"
                ],
                [
                  "48",
                  "6"
                ],
                [
                  "20",
                  "6"
                ],
                [
                  "51",
                  "5"
                ],
                [
                  "56",
                  "4"
                ],
                [
                  "49",
                  "4"
                ],
                [
                  "57",
                  "3"
                ],
                [
                  "55",
                  "3"
                ],
                [
                  "54",
                  "3"
                ],
                [
                  "47",
                  "2"
                ],
                [
                  "60",
                  "2"
                ],
                [
                  "-29",
                  "1"
                ],
                [
                  "329",
                  "1"
                ],
                [
                  "99999999999",
                  "1"
                ],
                [
                  "58",
                  "1"
                ],
                [
                  "62",
                  "1"
                ],
                [
                  "65",
                  "1"
                ],
                [
                  "-1726",
                  "1"
                ],
                [
                  "5",
                  "1"
                ],
                [
                  "53",
                  "1"
                ],
                [
                  "61",
                  "1"
                ],
                [
                  "8",
                  "1"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 53
              }
            },
            "text/plain": [
              "Age\n",
              " 29             85\n",
              " 32             81\n",
              " 26             75\n",
              " 27             70\n",
              " 33             70\n",
              " 28             67\n",
              " 31             67\n",
              " 34             65\n",
              " 30             63\n",
              " 25             61\n",
              " 35             54\n",
              " 23             51\n",
              " 24             46\n",
              " 37             43\n",
              " 38             39\n",
              " 36             37\n",
              " 39             33\n",
              " 40             33\n",
              " 43             28\n",
              " 41             21\n",
              " 22             21\n",
              " 42             20\n",
              " 21             16\n",
              " 45             12\n",
              " 46             12\n",
              " 44             11\n",
              " 19              9\n",
              " 18              7\n",
              " 50              6\n",
              " 48              6\n",
              " 20              6\n",
              " 51              5\n",
              " 56              4\n",
              " 49              4\n",
              " 57              3\n",
              " 55              3\n",
              " 54              3\n",
              " 47              2\n",
              " 60              2\n",
              "-29              1\n",
              " 329             1\n",
              " 99999999999     1\n",
              " 58              1\n",
              " 62              1\n",
              " 65              1\n",
              "-1726            1\n",
              " 5               1\n",
              " 53              1\n",
              " 61              1\n",
              " 8               1\n",
              " 11              1\n",
              "-1               1\n",
              " 72              1\n",
              "Name: count, dtype: int64"
            ]
          },
          "execution_count": 203,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['Age'].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1955c8a6",
      "metadata": {
        "id": "1955c8a6",
        "outputId": "dcbcc943-8b8c-4f71-8365-07c2369e951a"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Country",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "State",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "Self_Employed",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Family_History",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Treatment",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Work_Interfere",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "No_Employees",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Remote_Work",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Tech_Company",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Benefits",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Care_Options",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Wellness_Program",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Seek_Help",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Anonymity",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Leave",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Coworkers",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Supervisor",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_vs_Physical",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Obs_Consequence",
                  "rawType": "object",
                  "type": "string"
                }
              ],
              "ref": "cc5c83cb-d8b4-4086-8806-9a642479f5a7",
              "rows": [
                [
                  "143",
                  "-29",
                  "Male",
                  "United States",
                  "MN",
                  "No",
                  "No",
                  "No",
                  null,
                  "More than 1000",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "Don't know",
                  "Yes",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "715",
                  "-1726",
                  "male",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "1127",
                  "-1",
                  "p",
                  "United States",
                  "AL",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Often",
                  "1-5",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Very easy",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes"
                ]
              ],
              "shape": {
                "columns": 25,
                "rows": 3
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>Family_History</th>\n",
              "      <th>Treatment</th>\n",
              "      <th>Work_Interfere</th>\n",
              "      <th>No_Employees</th>\n",
              "      <th>Remote_Work</th>\n",
              "      <th>...</th>\n",
              "      <th>Anonymity</th>\n",
              "      <th>Leave</th>\n",
              "      <th>Mental_Health_Consequence</th>\n",
              "      <th>Physical_Health_Consequence</th>\n",
              "      <th>Coworkers</th>\n",
              "      <th>Supervisor</th>\n",
              "      <th>Mental_Health_Interview</th>\n",
              "      <th>Physical_Health_Interview</th>\n",
              "      <th>Mental_vs_Physical</th>\n",
              "      <th>Obs_Consequence</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>143</th>\n",
              "      <td>-29</td>\n",
              "      <td>Male</td>\n",
              "      <td>United States</td>\n",
              "      <td>MN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "      <td>More than 1000</td>\n",
              "      <td>Yes</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>715</th>\n",
              "      <td>-1726</td>\n",
              "      <td>male</td>\n",
              "      <td>United Kingdom</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Sometimes</td>\n",
              "      <td>26-100</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1127</th>\n",
              "      <td>-1</td>\n",
              "      <td>p</td>\n",
              "      <td>United States</td>\n",
              "      <td>AL</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>1-5</td>\n",
              "      <td>Yes</td>\n",
              "      <td>...</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Very easy</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>3 rows × 25 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "       Age Gender         Country State Self_Employed Family_History  \\\n",
              "143    -29   Male   United States    MN            No             No   \n",
              "715  -1726   male  United Kingdom   NaN            No             No   \n",
              "1127    -1      p   United States    AL           Yes            Yes   \n",
              "\n",
              "     Treatment Work_Interfere    No_Employees Remote_Work  ...   Anonymity  \\\n",
              "143         No            NaN  More than 1000         Yes  ...  Don't know   \n",
              "715        Yes      Sometimes          26-100          No  ...  Don't know   \n",
              "1127       Yes          Often             1-5         Yes  ...         Yes   \n",
              "\n",
              "                   Leave Mental_Health_Consequence  \\\n",
              "143           Don't know                        No   \n",
              "715   Somewhat difficult                       Yes   \n",
              "1127           Very easy                       Yes   \n",
              "\n",
              "     Physical_Health_Consequence     Coworkers Supervisor  \\\n",
              "143                           No  Some of them        Yes   \n",
              "715                           No            No         No   \n",
              "1127                         Yes           Yes        Yes   \n",
              "\n",
              "     Mental_Health_Interview Physical_Health_Interview Mental_vs_Physical  \\\n",
              "143                       No                        No         Don't know   \n",
              "715                       No                     Maybe         Don't know   \n",
              "1127                     Yes                       Yes                Yes   \n",
              "\n",
              "     Obs_Consequence  \n",
              "143               No  \n",
              "715               No  \n",
              "1127             Yes  \n",
              "\n",
              "[3 rows x 25 columns]"
            ]
          },
          "execution_count": 204,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df[df.Age<0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c584a5d3",
      "metadata": {
        "id": "c584a5d3"
      },
      "outputs": [],
      "source": [
        "# remove rows having age with negative value\n",
        "df = df[df['Age'] > 0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8189dd52",
      "metadata": {
        "id": "8189dd52",
        "outputId": "8e7a2a84-0e2c-4f07-f9d7-460de8fab6e7"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Country",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "State",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "Self_Employed",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "Family_History",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Treatment",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Work_Interfere",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "No_Employees",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Remote_Work",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Tech_Company",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Benefits",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Care_Options",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Wellness_Program",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Seek_Help",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Anonymity",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Leave",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Coworkers",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Supervisor",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_vs_Physical",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Obs_Consequence",
                  "rawType": "object",
                  "type": "string"
                }
              ],
              "ref": "50293b39-310c-4544-a1ba-23e6a8aaf473",
              "rows": [
                [
                  "0",
                  "37",
                  "Female",
                  "United States",
                  "IL",
                  null,
                  "No",
                  "Yes",
                  "Often",
                  "6-25",
                  "No",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "No",
                  "Yes",
                  "Yes",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "1",
                  "44",
                  "M",
                  "United States",
                  "IN",
                  null,
                  "No",
                  "No",
                  "Rarely",
                  "More than 1000",
                  "No",
                  "No",
                  "Don't know",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "2",
                  "32",
                  "Male",
                  "Canada",
                  null,
                  null,
                  "No",
                  "No",
                  "Rarely",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No"
                ],
                [
                  "3",
                  "31",
                  "Male",
                  "United Kingdom",
                  null,
                  null,
                  "Yes",
                  "Yes",
                  "Often",
                  "26-100",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "Somewhat difficult",
                  "Yes",
                  "Yes",
                  "Some of them",
                  "No",
                  "Maybe",
                  "Maybe",
                  "No",
                  "Yes"
                ],
                [
                  "4",
                  "31",
                  "Male",
                  "United States",
                  "TX",
                  null,
                  "No",
                  "No",
                  "Never",
                  "100-500",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "5",
                  "33",
                  "Male",
                  "United States",
                  "TN",
                  null,
                  "Yes",
                  "No",
                  "Sometimes",
                  "6-25",
                  "No",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "6",
                  "35",
                  "Female",
                  "United States",
                  "MI",
                  null,
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "1-5",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Somewhat difficult",
                  "Maybe",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "7",
                  "39",
                  "M",
                  "Canada",
                  null,
                  null,
                  "No",
                  "No",
                  "Never",
                  "1-5",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "8",
                  "42",
                  "Female",
                  "United States",
                  "IL",
                  null,
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "100-500",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "Very difficult",
                  "Maybe",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "9",
                  "23",
                  "Male",
                  "Canada",
                  null,
                  null,
                  "No",
                  "No",
                  "Never",
                  "26-100",
                  "No",
                  "Yes",
                  "Don't know",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "10",
                  "31",
                  "Male",
                  "United States",
                  "OH",
                  null,
                  "No",
                  "Yes",
                  "Sometimes",
                  "6-25",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "11",
                  "29",
                  "male",
                  "Bulgaria",
                  null,
                  null,
                  "No",
                  "No",
                  "Never",
                  "100-500",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "12",
                  "42",
                  "female",
                  "United States",
                  "CA",
                  null,
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "No",
                  "Yes"
                ],
                [
                  "13",
                  "36",
                  "Male",
                  "United States",
                  "CT",
                  null,
                  "Yes",
                  "No",
                  "Never",
                  "500-1000",
                  "No",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "14",
                  "27",
                  "Male",
                  "Canada",
                  null,
                  null,
                  "No",
                  "No",
                  "Never",
                  "6-25",
                  "No",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Some of them",
                  "Maybe",
                  "Yes",
                  "Yes",
                  "No"
                ],
                [
                  "15",
                  "29",
                  "female",
                  "United States",
                  "IL",
                  null,
                  "Yes",
                  "Yes",
                  "Rarely",
                  "26-100",
                  "No",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Yes",
                  "Some of them",
                  "Maybe",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "16",
                  "23",
                  "Male",
                  "United Kingdom",
                  null,
                  null,
                  "No",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Very easy",
                  "Maybe",
                  "No",
                  "Some of them",
                  "No",
                  "Maybe",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "17",
                  "32",
                  "Male",
                  "United States",
                  "TN",
                  null,
                  "No",
                  "Yes",
                  "Sometimes",
                  "6-25",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "18",
                  "46",
                  "male",
                  "United States",
                  "MD",
                  "Yes",
                  "Yes",
                  "No",
                  "Sometimes",
                  "1-5",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "Yes",
                  "Don't know",
                  "Yes",
                  "Very easy",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes"
                ],
                [
                  "19",
                  "36",
                  "Male",
                  "France",
                  null,
                  "Yes",
                  "Yes",
                  "No",
                  null,
                  "6-25",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Some of them",
                  "Maybe",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "20",
                  "29",
                  "Male",
                  "United States",
                  "NY",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "100-500",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "Somewhat difficult",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "21",
                  "31",
                  "male",
                  "United States",
                  "NC",
                  "Yes",
                  "No",
                  "No",
                  "Never",
                  "1-5",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Yes",
                  "Somewhat difficult",
                  "No",
                  "No",
                  "Some of them",
                  "Some of them",
                  "No",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "22",
                  "46",
                  "Male",
                  "United States",
                  "MA",
                  "No",
                  "No",
                  "Yes",
                  "Often",
                  "26-100",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "23",
                  "41",
                  "Male",
                  "United States",
                  "IA",
                  "No",
                  "No",
                  "Yes",
                  "Never",
                  "More than 1000",
                  "No",
                  "No",
                  "Don't know",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "24",
                  "33",
                  "male",
                  "United States",
                  "CA",
                  "No",
                  "Yes",
                  "Yes",
                  "Rarely",
                  "26-100",
                  "No",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "Don't know",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "25",
                  "35",
                  "male",
                  "United States",
                  "TN",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "More than 1000",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "No",
                  "Very easy",
                  "Yes",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No"
                ],
                [
                  "26",
                  "33",
                  "male",
                  "United States",
                  "TN",
                  "No",
                  "No",
                  "No",
                  null,
                  "1-5",
                  "No",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "27",
                  "35",
                  "Female",
                  "United States",
                  "CA",
                  "No",
                  "Yes",
                  "Yes",
                  "Rarely",
                  "6-25",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "28",
                  "34",
                  "male",
                  "United States",
                  "OH",
                  "No",
                  "No",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Somewhat difficult",
                  "No",
                  "No",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "29",
                  "37",
                  "Male",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "No",
                  "Sometimes",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Very difficult",
                  "Yes",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "30",
                  "32",
                  "Male",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "No",
                  "Never",
                  "6-25",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Yes",
                  "Yes",
                  "Some of them",
                  "Some of them",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "31",
                  "31",
                  "Male",
                  "United States",
                  "PA",
                  "Yes",
                  "Yes",
                  "No",
                  "Rarely",
                  "1-5",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Yes"
                ],
                [
                  "32",
                  "30",
                  "male",
                  "United Kingdom",
                  null,
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "500-1000",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "Yes",
                  "Somewhat easy",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "33",
                  "42",
                  "Male",
                  "United States",
                  "WA",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Very easy",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Some of them",
                  "Maybe",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "34",
                  "40",
                  "female",
                  "United States",
                  "WI",
                  "No",
                  "No",
                  "Yes",
                  "Sometimes",
                  "1-5",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "Some of them",
                  "No",
                  "No",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "35",
                  "27",
                  "Male",
                  "United States",
                  "NY",
                  "No",
                  "No",
                  "Yes",
                  "Rarely",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Very easy",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "36",
                  "29",
                  "Male",
                  "Canada",
                  null,
                  "No",
                  "No",
                  "No",
                  "Rarely",
                  "1-5",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Very easy",
                  "Yes",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "37",
                  "38",
                  "Male",
                  "Portugal",
                  null,
                  "No",
                  "No",
                  "No",
                  null,
                  "100-500",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat easy",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Some of them",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "38",
                  "50",
                  "M",
                  "United States",
                  "IN",
                  "No",
                  "No",
                  "No",
                  null,
                  "100-500",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "39",
                  "35",
                  "M",
                  "United States",
                  "TX",
                  "No",
                  "No",
                  "Yes",
                  "Rarely",
                  "More than 1000",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "Very easy",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "40",
                  "24",
                  "Male",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "Yes",
                  "Sometimes",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "Yes",
                  "No",
                  "Yes"
                ],
                [
                  "41",
                  "35",
                  "Male",
                  "United States",
                  "MI",
                  "No",
                  "No",
                  "No",
                  null,
                  "More than 1000",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "Don't know",
                  "Yes",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "Yes",
                  "Some of them",
                  "No",
                  "No",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "42",
                  "27",
                  "Male",
                  "Canada",
                  null,
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "1-5",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "Very difficult",
                  "Maybe",
                  "No",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "Yes",
                  "No"
                ],
                [
                  "43",
                  "18",
                  "Male",
                  "Netherlands",
                  null,
                  "No",
                  "No",
                  "No",
                  "Often",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "Not sure",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "Maybe",
                  "No",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "44",
                  "30",
                  "Male",
                  "United States",
                  "IN",
                  "No",
                  "No",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "No",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "45",
                  "38",
                  "Female",
                  "United States",
                  "TX",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "No"
                ],
                [
                  "46",
                  "28",
                  "Male",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "No",
                  null,
                  "26-100",
                  "No",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "Maybe",
                  "Some of them",
                  "Yes",
                  "Maybe",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "47",
                  "34",
                  "Male",
                  "United States",
                  "TN",
                  "No",
                  "No",
                  "No",
                  null,
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "48",
                  "26",
                  "m",
                  "Canada",
                  null,
                  "Yes",
                  "No",
                  "No",
                  "Sometimes",
                  "1-5",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "No"
                ],
                [
                  "49",
                  "30",
                  "male",
                  "United States",
                  "IL",
                  "No",
                  "Yes",
                  "Yes",
                  "Rarely",
                  "26-100",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ]
              ],
              "shape": {
                "columns": 25,
                "rows": 1252
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>Family_History</th>\n",
              "      <th>Treatment</th>\n",
              "      <th>Work_Interfere</th>\n",
              "      <th>No_Employees</th>\n",
              "      <th>Remote_Work</th>\n",
              "      <th>...</th>\n",
              "      <th>Anonymity</th>\n",
              "      <th>Leave</th>\n",
              "      <th>Mental_Health_Consequence</th>\n",
              "      <th>Physical_Health_Consequence</th>\n",
              "      <th>Coworkers</th>\n",
              "      <th>Supervisor</th>\n",
              "      <th>Mental_Health_Interview</th>\n",
              "      <th>Physical_Health_Interview</th>\n",
              "      <th>Mental_vs_Physical</th>\n",
              "      <th>Obs_Consequence</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>37</td>\n",
              "      <td>Female</td>\n",
              "      <td>United States</td>\n",
              "      <td>IL</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>6-25</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Somewhat easy</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>44</td>\n",
              "      <td>M</td>\n",
              "      <td>United States</td>\n",
              "      <td>IN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Rarely</td>\n",
              "      <td>More than 1000</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>32</td>\n",
              "      <td>Male</td>\n",
              "      <td>Canada</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Rarely</td>\n",
              "      <td>6-25</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>31</td>\n",
              "      <td>Male</td>\n",
              "      <td>United Kingdom</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>26-100</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>No</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>No</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>31</td>\n",
              "      <td>Male</td>\n",
              "      <td>United States</td>\n",
              "      <td>TX</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Never</td>\n",
              "      <td>100-500</td>\n",
              "      <td>Yes</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1254</th>\n",
              "      <td>26</td>\n",
              "      <td>male</td>\n",
              "      <td>United Kingdom</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>NaN</td>\n",
              "      <td>26-100</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Somewhat easy</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1255</th>\n",
              "      <td>32</td>\n",
              "      <td>Male</td>\n",
              "      <td>United States</td>\n",
              "      <td>IL</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>26-100</td>\n",
              "      <td>Yes</td>\n",
              "      <td>...</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1256</th>\n",
              "      <td>34</td>\n",
              "      <td>male</td>\n",
              "      <td>United States</td>\n",
              "      <td>CA</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Sometimes</td>\n",
              "      <td>More than 1000</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1257</th>\n",
              "      <td>46</td>\n",
              "      <td>f</td>\n",
              "      <td>United States</td>\n",
              "      <td>NC</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "      <td>100-500</td>\n",
              "      <td>Yes</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1258</th>\n",
              "      <td>25</td>\n",
              "      <td>Male</td>\n",
              "      <td>United States</td>\n",
              "      <td>IL</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Sometimes</td>\n",
              "      <td>26-100</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1252 rows × 25 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      Age  Gender         Country State Self_Employed Family_History  \\\n",
              "0      37  Female   United States    IL           NaN             No   \n",
              "1      44       M   United States    IN           NaN             No   \n",
              "2      32    Male          Canada   NaN           NaN             No   \n",
              "3      31    Male  United Kingdom   NaN           NaN            Yes   \n",
              "4      31    Male   United States    TX           NaN             No   \n",
              "...   ...     ...             ...   ...           ...            ...   \n",
              "1254   26    male  United Kingdom   NaN            No             No   \n",
              "1255   32    Male   United States    IL            No            Yes   \n",
              "1256   34    male   United States    CA            No            Yes   \n",
              "1257   46       f   United States    NC            No             No   \n",
              "1258   25    Male   United States    IL            No            Yes   \n",
              "\n",
              "     Treatment Work_Interfere    No_Employees Remote_Work  ...   Anonymity  \\\n",
              "0          Yes          Often            6-25          No  ...         Yes   \n",
              "1           No         Rarely  More than 1000          No  ...  Don't know   \n",
              "2           No         Rarely            6-25          No  ...  Don't know   \n",
              "3          Yes          Often          26-100          No  ...          No   \n",
              "4           No          Never         100-500         Yes  ...  Don't know   \n",
              "...        ...            ...             ...         ...  ...         ...   \n",
              "1254       Yes            NaN          26-100          No  ...  Don't know   \n",
              "1255       Yes          Often          26-100         Yes  ...         Yes   \n",
              "1256       Yes      Sometimes  More than 1000          No  ...  Don't know   \n",
              "1257        No            NaN         100-500         Yes  ...  Don't know   \n",
              "1258       Yes      Sometimes          26-100          No  ...         Yes   \n",
              "\n",
              "                   Leave Mental_Health_Consequence  \\\n",
              "0          Somewhat easy                        No   \n",
              "1             Don't know                     Maybe   \n",
              "2     Somewhat difficult                        No   \n",
              "3     Somewhat difficult                       Yes   \n",
              "4             Don't know                        No   \n",
              "...                  ...                       ...   \n",
              "1254       Somewhat easy                        No   \n",
              "1255  Somewhat difficult                        No   \n",
              "1256  Somewhat difficult                       Yes   \n",
              "1257          Don't know                       Yes   \n",
              "1258          Don't know                     Maybe   \n",
              "\n",
              "     Physical_Health_Consequence     Coworkers    Supervisor  \\\n",
              "0                             No  Some of them           Yes   \n",
              "1                             No            No            No   \n",
              "2                             No           Yes           Yes   \n",
              "3                            Yes  Some of them            No   \n",
              "4                             No  Some of them           Yes   \n",
              "...                          ...           ...           ...   \n",
              "1254                          No  Some of them  Some of them   \n",
              "1255                          No  Some of them           Yes   \n",
              "1256                         Yes            No            No   \n",
              "1257                          No            No            No   \n",
              "1258                          No  Some of them            No   \n",
              "\n",
              "     Mental_Health_Interview Physical_Health_Interview Mental_vs_Physical  \\\n",
              "0                         No                     Maybe                Yes   \n",
              "1                         No                        No         Don't know   \n",
              "2                        Yes                       Yes                 No   \n",
              "3                      Maybe                     Maybe                 No   \n",
              "4                        Yes                       Yes         Don't know   \n",
              "...                      ...                       ...                ...   \n",
              "1254                      No                        No         Don't know   \n",
              "1255                      No                        No                Yes   \n",
              "1256                      No                        No                 No   \n",
              "1257                      No                        No                 No   \n",
              "1258                      No                        No         Don't know   \n",
              "\n",
              "     Obs_Consequence  \n",
              "0                 No  \n",
              "1                 No  \n",
              "2                 No  \n",
              "3                Yes  \n",
              "4                 No  \n",
              "...              ...  \n",
              "1254              No  \n",
              "1255              No  \n",
              "1256              No  \n",
              "1257              No  \n",
              "1258              No  \n",
              "\n",
              "[1252 rows x 25 columns]"
            ]
          },
          "execution_count": 206,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "2b072266",
      "metadata": {
        "id": "2b072266",
        "outputId": "3911f894-2698-48ac-9d50-ba3e149255e9"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "count",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "5d01bc3c-500f-4bdf-be1e-f8320cefa3a2",
              "rows": [
                [
                  "29",
                  "85"
                ],
                [
                  "32",
                  "81"
                ],
                [
                  "26",
                  "75"
                ],
                [
                  "33",
                  "70"
                ],
                [
                  "27",
                  "70"
                ],
                [
                  "31",
                  "67"
                ],
                [
                  "28",
                  "67"
                ],
                [
                  "34",
                  "65"
                ],
                [
                  "30",
                  "63"
                ],
                [
                  "25",
                  "61"
                ],
                [
                  "35",
                  "54"
                ],
                [
                  "23",
                  "51"
                ],
                [
                  "24",
                  "46"
                ],
                [
                  "37",
                  "43"
                ],
                [
                  "38",
                  "39"
                ],
                [
                  "36",
                  "37"
                ],
                [
                  "40",
                  "33"
                ],
                [
                  "39",
                  "33"
                ],
                [
                  "43",
                  "28"
                ],
                [
                  "22",
                  "21"
                ],
                [
                  "41",
                  "21"
                ],
                [
                  "42",
                  "20"
                ],
                [
                  "21",
                  "16"
                ],
                [
                  "46",
                  "12"
                ],
                [
                  "45",
                  "12"
                ],
                [
                  "44",
                  "11"
                ],
                [
                  "19",
                  "9"
                ],
                [
                  "18",
                  "7"
                ],
                [
                  "50",
                  "6"
                ],
                [
                  "48",
                  "6"
                ],
                [
                  "20",
                  "6"
                ],
                [
                  "51",
                  "5"
                ],
                [
                  "49",
                  "4"
                ],
                [
                  "56",
                  "4"
                ],
                [
                  "57",
                  "3"
                ],
                [
                  "54",
                  "3"
                ],
                [
                  "55",
                  "3"
                ],
                [
                  "60",
                  "2"
                ],
                [
                  "47",
                  "2"
                ],
                [
                  "329",
                  "1"
                ],
                [
                  "58",
                  "1"
                ],
                [
                  "99999999999",
                  "1"
                ],
                [
                  "62",
                  "1"
                ],
                [
                  "65",
                  "1"
                ],
                [
                  "5",
                  "1"
                ],
                [
                  "53",
                  "1"
                ],
                [
                  "61",
                  "1"
                ],
                [
                  "8",
                  "1"
                ],
                [
                  "11",
                  "1"
                ],
                [
                  "72",
                  "1"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 50
              }
            },
            "text/plain": [
              "Age\n",
              "29             85\n",
              "32             81\n",
              "26             75\n",
              "33             70\n",
              "27             70\n",
              "31             67\n",
              "28             67\n",
              "34             65\n",
              "30             63\n",
              "25             61\n",
              "35             54\n",
              "23             51\n",
              "24             46\n",
              "37             43\n",
              "38             39\n",
              "36             37\n",
              "40             33\n",
              "39             33\n",
              "43             28\n",
              "22             21\n",
              "41             21\n",
              "42             20\n",
              "21             16\n",
              "46             12\n",
              "45             12\n",
              "44             11\n",
              "19              9\n",
              "18              7\n",
              "50              6\n",
              "48              6\n",
              "20              6\n",
              "51              5\n",
              "49              4\n",
              "56              4\n",
              "57              3\n",
              "54              3\n",
              "55              3\n",
              "60              2\n",
              "47              2\n",
              "329             1\n",
              "58              1\n",
              "99999999999     1\n",
              "62              1\n",
              "65              1\n",
              "5               1\n",
              "53              1\n",
              "61              1\n",
              "8               1\n",
              "11              1\n",
              "72              1\n",
              "Name: count, dtype: int64"
            ]
          },
          "execution_count": 207,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['Age'].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "34fe0cba",
      "metadata": {
        "id": "34fe0cba"
      },
      "outputs": [],
      "source": [
        "df = df[df['Age'] <= 72]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "61086923",
      "metadata": {
        "id": "61086923",
        "outputId": "71c319e1-1095-42cf-8d7b-d23e26487a9b"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "count",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "177cb806-1796-4c71-a493-e0f2a01f980a",
              "rows": [
                [
                  "29",
                  "85"
                ],
                [
                  "32",
                  "81"
                ],
                [
                  "26",
                  "75"
                ],
                [
                  "27",
                  "70"
                ],
                [
                  "33",
                  "70"
                ],
                [
                  "31",
                  "67"
                ],
                [
                  "28",
                  "67"
                ],
                [
                  "34",
                  "65"
                ],
                [
                  "30",
                  "63"
                ],
                [
                  "25",
                  "61"
                ],
                [
                  "35",
                  "54"
                ],
                [
                  "23",
                  "51"
                ],
                [
                  "24",
                  "46"
                ],
                [
                  "37",
                  "43"
                ],
                [
                  "38",
                  "39"
                ],
                [
                  "36",
                  "37"
                ],
                [
                  "39",
                  "33"
                ],
                [
                  "40",
                  "33"
                ],
                [
                  "43",
                  "28"
                ],
                [
                  "41",
                  "21"
                ],
                [
                  "22",
                  "21"
                ],
                [
                  "42",
                  "20"
                ],
                [
                  "21",
                  "16"
                ],
                [
                  "46",
                  "12"
                ],
                [
                  "45",
                  "12"
                ],
                [
                  "44",
                  "11"
                ],
                [
                  "19",
                  "9"
                ],
                [
                  "18",
                  "7"
                ],
                [
                  "50",
                  "6"
                ],
                [
                  "48",
                  "6"
                ],
                [
                  "20",
                  "6"
                ],
                [
                  "51",
                  "5"
                ],
                [
                  "56",
                  "4"
                ],
                [
                  "49",
                  "4"
                ],
                [
                  "57",
                  "3"
                ],
                [
                  "54",
                  "3"
                ],
                [
                  "55",
                  "3"
                ],
                [
                  "60",
                  "2"
                ],
                [
                  "47",
                  "2"
                ],
                [
                  "58",
                  "1"
                ],
                [
                  "62",
                  "1"
                ],
                [
                  "65",
                  "1"
                ],
                [
                  "5",
                  "1"
                ],
                [
                  "53",
                  "1"
                ],
                [
                  "61",
                  "1"
                ],
                [
                  "8",
                  "1"
                ],
                [
                  "11",
                  "1"
                ],
                [
                  "72",
                  "1"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 48
              }
            },
            "text/plain": [
              "Age\n",
              "29    85\n",
              "32    81\n",
              "26    75\n",
              "27    70\n",
              "33    70\n",
              "31    67\n",
              "28    67\n",
              "34    65\n",
              "30    63\n",
              "25    61\n",
              "35    54\n",
              "23    51\n",
              "24    46\n",
              "37    43\n",
              "38    39\n",
              "36    37\n",
              "39    33\n",
              "40    33\n",
              "43    28\n",
              "41    21\n",
              "22    21\n",
              "42    20\n",
              "21    16\n",
              "46    12\n",
              "45    12\n",
              "44    11\n",
              "19     9\n",
              "18     7\n",
              "50     6\n",
              "48     6\n",
              "20     6\n",
              "51     5\n",
              "56     4\n",
              "49     4\n",
              "57     3\n",
              "54     3\n",
              "55     3\n",
              "60     2\n",
              "47     2\n",
              "58     1\n",
              "62     1\n",
              "65     1\n",
              "5      1\n",
              "53     1\n",
              "61     1\n",
              "8      1\n",
              "11     1\n",
              "72     1\n",
              "Name: count, dtype: int64"
            ]
          },
          "execution_count": 209,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['Age'].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6bc7f2fc",
      "metadata": {
        "id": "6bc7f2fc"
      },
      "outputs": [],
      "source": [
        "# age should be greater than or equal to 18\n",
        "\n",
        "df = df[df['Age'] >= 18]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "803b3aaa",
      "metadata": {
        "id": "803b3aaa",
        "outputId": "d7cc312f-a410-438e-91be-5aed5fa12a98"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "count",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "7f38db9d-360f-4d6e-aea9-21ac5881320a",
              "rows": [
                [
                  "29",
                  "85"
                ],
                [
                  "32",
                  "81"
                ],
                [
                  "26",
                  "75"
                ],
                [
                  "27",
                  "70"
                ],
                [
                  "33",
                  "70"
                ],
                [
                  "28",
                  "67"
                ],
                [
                  "31",
                  "67"
                ],
                [
                  "34",
                  "65"
                ],
                [
                  "30",
                  "63"
                ],
                [
                  "25",
                  "61"
                ],
                [
                  "35",
                  "54"
                ],
                [
                  "23",
                  "51"
                ],
                [
                  "24",
                  "46"
                ],
                [
                  "37",
                  "43"
                ],
                [
                  "38",
                  "39"
                ],
                [
                  "36",
                  "37"
                ],
                [
                  "39",
                  "33"
                ],
                [
                  "40",
                  "33"
                ],
                [
                  "43",
                  "28"
                ],
                [
                  "41",
                  "21"
                ],
                [
                  "22",
                  "21"
                ],
                [
                  "42",
                  "20"
                ],
                [
                  "21",
                  "16"
                ],
                [
                  "45",
                  "12"
                ],
                [
                  "46",
                  "12"
                ],
                [
                  "44",
                  "11"
                ],
                [
                  "19",
                  "9"
                ],
                [
                  "18",
                  "7"
                ],
                [
                  "50",
                  "6"
                ],
                [
                  "20",
                  "6"
                ],
                [
                  "48",
                  "6"
                ],
                [
                  "51",
                  "5"
                ],
                [
                  "56",
                  "4"
                ],
                [
                  "49",
                  "4"
                ],
                [
                  "55",
                  "3"
                ],
                [
                  "57",
                  "3"
                ],
                [
                  "54",
                  "3"
                ],
                [
                  "47",
                  "2"
                ],
                [
                  "60",
                  "2"
                ],
                [
                  "58",
                  "1"
                ],
                [
                  "62",
                  "1"
                ],
                [
                  "65",
                  "1"
                ],
                [
                  "53",
                  "1"
                ],
                [
                  "61",
                  "1"
                ],
                [
                  "72",
                  "1"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 45
              }
            },
            "text/plain": [
              "Age\n",
              "29    85\n",
              "32    81\n",
              "26    75\n",
              "27    70\n",
              "33    70\n",
              "28    67\n",
              "31    67\n",
              "34    65\n",
              "30    63\n",
              "25    61\n",
              "35    54\n",
              "23    51\n",
              "24    46\n",
              "37    43\n",
              "38    39\n",
              "36    37\n",
              "39    33\n",
              "40    33\n",
              "43    28\n",
              "41    21\n",
              "22    21\n",
              "42    20\n",
              "21    16\n",
              "45    12\n",
              "46    12\n",
              "44    11\n",
              "19     9\n",
              "18     7\n",
              "50     6\n",
              "20     6\n",
              "48     6\n",
              "51     5\n",
              "56     4\n",
              "49     4\n",
              "55     3\n",
              "57     3\n",
              "54     3\n",
              "47     2\n",
              "60     2\n",
              "58     1\n",
              "62     1\n",
              "65     1\n",
              "53     1\n",
              "61     1\n",
              "72     1\n",
              "Name: count, dtype: int64"
            ]
          },
          "execution_count": 211,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['Age'].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "20f9f68f",
      "metadata": {
        "id": "20f9f68f",
        "outputId": "401dba51-d705-47a4-e472-384ace44c06d"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "count",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "7fc00dd8-dd7c-439a-b8a9-9a5761adb93a",
              "rows": [
                [
                  "Male",
                  "611"
                ],
                [
                  "male",
                  "202"
                ],
                [
                  "Female",
                  "121"
                ],
                [
                  "M",
                  "115"
                ],
                [
                  "female",
                  "62"
                ],
                [
                  "F",
                  "38"
                ],
                [
                  "m",
                  "34"
                ],
                [
                  "f",
                  "15"
                ],
                [
                  "Make",
                  "4"
                ],
                [
                  "Woman",
                  "3"
                ],
                [
                  "Male ",
                  "3"
                ],
                [
                  "Female ",
                  "2"
                ],
                [
                  "Cis Male",
                  "2"
                ],
                [
                  "Man",
                  "2"
                ],
                [
                  "Female (trans)",
                  "2"
                ],
                [
                  "something kinda male?",
                  "1"
                ],
                [
                  "Trans-female",
                  "1"
                ],
                [
                  "Cis Female",
                  "1"
                ],
                [
                  "Male-ish",
                  "1"
                ],
                [
                  "maile",
                  "1"
                ],
                [
                  "queer/she/they",
                  "1"
                ],
                [
                  "Male (CIS)",
                  "1"
                ],
                [
                  "woman",
                  "1"
                ],
                [
                  "Nah",
                  "1"
                ],
                [
                  "fluid",
                  "1"
                ],
                [
                  "Enby",
                  "1"
                ],
                [
                  "Genderqueer",
                  "1"
                ],
                [
                  "non-binary",
                  "1"
                ],
                [
                  "Femake",
                  "1"
                ],
                [
                  "Mal",
                  "1"
                ],
                [
                  "cis-female/femme",
                  "1"
                ],
                [
                  "Agender",
                  "1"
                ],
                [
                  "Androgyne",
                  "1"
                ],
                [
                  "male leaning androgynous",
                  "1"
                ],
                [
                  "Guy (-ish) ^_^",
                  "1"
                ],
                [
                  "Trans woman",
                  "1"
                ],
                [
                  "msle",
                  "1"
                ],
                [
                  "Neuter",
                  "1"
                ],
                [
                  "queer",
                  "1"
                ],
                [
                  "Female (cis)",
                  "1"
                ],
                [
                  "Mail",
                  "1"
                ],
                [
                  "cis male",
                  "1"
                ],
                [
                  "Malr",
                  "1"
                ],
                [
                  "femail",
                  "1"
                ],
                [
                  "Cis Man",
                  "1"
                ],
                [
                  "ostensibly male, unsure what that really means",
                  "1"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 46
              }
            },
            "text/plain": [
              "Gender\n",
              "Male                                              611\n",
              "male                                              202\n",
              "Female                                            121\n",
              "M                                                 115\n",
              "female                                             62\n",
              "F                                                  38\n",
              "m                                                  34\n",
              "f                                                  15\n",
              "Make                                                4\n",
              "Woman                                               3\n",
              "Male                                                3\n",
              "Female                                              2\n",
              "Cis Male                                            2\n",
              "Man                                                 2\n",
              "Female (trans)                                      2\n",
              "something kinda male?                               1\n",
              "Trans-female                                        1\n",
              "Cis Female                                          1\n",
              "Male-ish                                            1\n",
              "maile                                               1\n",
              "queer/she/they                                      1\n",
              "Male (CIS)                                          1\n",
              "woman                                               1\n",
              "Nah                                                 1\n",
              "fluid                                               1\n",
              "Enby                                                1\n",
              "Genderqueer                                         1\n",
              "non-binary                                          1\n",
              "Femake                                              1\n",
              "Mal                                                 1\n",
              "cis-female/femme                                    1\n",
              "Agender                                             1\n",
              "Androgyne                                           1\n",
              "male leaning androgynous                            1\n",
              "Guy (-ish) ^_^                                      1\n",
              "Trans woman                                         1\n",
              "msle                                                1\n",
              "Neuter                                              1\n",
              "queer                                               1\n",
              "Female (cis)                                        1\n",
              "Mail                                                1\n",
              "cis male                                            1\n",
              "Malr                                                1\n",
              "femail                                              1\n",
              "Cis Man                                             1\n",
              "ostensibly male, unsure what that really means      1\n",
              "Name: count, dtype: int64"
            ]
          },
          "execution_count": 212,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['Gender'].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d993380a",
      "metadata": {
        "id": "d993380a"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "a39e2e26",
      "metadata": {
        "id": "a39e2e26"
      },
      "outputs": [],
      "source": [
        "df = df[df.groupby('Gender')['Gender'].transform('count') > 1]\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "468f7492",
      "metadata": {
        "id": "468f7492",
        "outputId": "f96af9e2-8175-461e-9bc0-c5d80d7e8e01"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Country",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "State",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Self_Employed",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Family_History",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Treatment",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Work_Interfere",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "No_Employees",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Remote_Work",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Tech_Company",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Benefits",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Care_Options",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Wellness_Program",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Seek_Help",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Anonymity",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Leave",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_Health_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Physical_Health_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Coworkers",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Supervisor",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_Health_Interview",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Physical_Health_Interview",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_vs_Physical",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Obs_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "8d99d3a3-1786-4035-823f-1bdd6a9ebb6f",
              "rows": [
                [
                  "Cis Male",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2"
                ],
                [
                  "F",
                  "38",
                  "38",
                  "34",
                  "38",
                  "38",
                  "38",
                  "31",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38",
                  "38"
                ],
                [
                  "Female",
                  "121",
                  "121",
                  "80",
                  "118",
                  "121",
                  "121",
                  "106",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121",
                  "121"
                ],
                [
                  "Female ",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2"
                ],
                [
                  "Female (trans)",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2"
                ],
                [
                  "M",
                  "115",
                  "115",
                  "90",
                  "113",
                  "115",
                  "115",
                  "86",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115",
                  "115"
                ],
                [
                  "Make",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4"
                ],
                [
                  "Male",
                  "611",
                  "611",
                  "340",
                  "601",
                  "611",
                  "611",
                  "479",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611",
                  "611"
                ],
                [
                  "Male ",
                  "3",
                  "3",
                  "1",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3"
                ],
                [
                  "Man",
                  "2",
                  "2",
                  "1",
                  "2",
                  "2",
                  "2",
                  "0",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2"
                ],
                [
                  "Woman",
                  "3",
                  "3",
                  "2",
                  "3",
                  "3",
                  "3",
                  "1",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3"
                ],
                [
                  "f",
                  "15",
                  "15",
                  "11",
                  "15",
                  "15",
                  "15",
                  "13",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15",
                  "15"
                ],
                [
                  "female",
                  "62",
                  "62",
                  "44",
                  "60",
                  "62",
                  "62",
                  "53",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62",
                  "62"
                ],
                [
                  "m",
                  "34",
                  "34",
                  "18",
                  "34",
                  "34",
                  "34",
                  "23",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34",
                  "34"
                ],
                [
                  "male",
                  "202",
                  "202",
                  "89",
                  "201",
                  "202",
                  "202",
                  "154",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202",
                  "202"
                ]
              ],
              "shape": {
                "columns": 24,
                "rows": 15
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>Family_History</th>\n",
              "      <th>Treatment</th>\n",
              "      <th>Work_Interfere</th>\n",
              "      <th>No_Employees</th>\n",
              "      <th>Remote_Work</th>\n",
              "      <th>Tech_Company</th>\n",
              "      <th>...</th>\n",
              "      <th>Anonymity</th>\n",
              "      <th>Leave</th>\n",
              "      <th>Mental_Health_Consequence</th>\n",
              "      <th>Physical_Health_Consequence</th>\n",
              "      <th>Coworkers</th>\n",
              "      <th>Supervisor</th>\n",
              "      <th>Mental_Health_Interview</th>\n",
              "      <th>Physical_Health_Interview</th>\n",
              "      <th>Mental_vs_Physical</th>\n",
              "      <th>Obs_Consequence</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Gender</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Cis Male</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>F</th>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>34</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>31</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>...</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "      <td>38</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Female</th>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>80</td>\n",
              "      <td>118</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>106</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>...</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "      <td>121</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Female</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Female (trans)</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>M</th>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>90</td>\n",
              "      <td>113</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>86</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>...</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "      <td>115</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Make</th>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>...</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Male</th>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>340</td>\n",
              "      <td>601</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>479</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>...</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "      <td>611</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Male</th>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Man</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Woman</th>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>f</th>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>13</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>...</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "      <td>15</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>female</th>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>44</td>\n",
              "      <td>60</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>53</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>...</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "      <td>62</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>m</th>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>18</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>23</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>...</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "      <td>34</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>male</th>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>89</td>\n",
              "      <td>201</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>154</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>...</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "      <td>202</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>15 rows × 24 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                Age  Country  State  Self_Employed  Family_History  Treatment  \\\n",
              "Gender                                                                          \n",
              "Cis Male          2        2      2              2               2          2   \n",
              "F                38       38     34             38              38         38   \n",
              "Female          121      121     80            118             121        121   \n",
              "Female            2        2      2              2               2          2   \n",
              "Female (trans)    2        2      2              2               2          2   \n",
              "M               115      115     90            113             115        115   \n",
              "Make              4        4      4              4               4          4   \n",
              "Male            611      611    340            601             611        611   \n",
              "Male              3        3      1              3               3          3   \n",
              "Man               2        2      1              2               2          2   \n",
              "Woman             3        3      2              3               3          3   \n",
              "f                15       15     11             15              15         15   \n",
              "female           62       62     44             60              62         62   \n",
              "m                34       34     18             34              34         34   \n",
              "male            202      202     89            201             202        202   \n",
              "\n",
              "                Work_Interfere  No_Employees  Remote_Work  Tech_Company  ...  \\\n",
              "Gender                                                                   ...   \n",
              "Cis Male                     2             2            2             2  ...   \n",
              "F                           31            38           38            38  ...   \n",
              "Female                     106           121          121           121  ...   \n",
              "Female                       2             2            2             2  ...   \n",
              "Female (trans)               2             2            2             2  ...   \n",
              "M                           86           115          115           115  ...   \n",
              "Make                         4             4            4             4  ...   \n",
              "Male                       479           611          611           611  ...   \n",
              "Male                         3             3            3             3  ...   \n",
              "Man                          0             2            2             2  ...   \n",
              "Woman                        1             3            3             3  ...   \n",
              "f                           13            15           15            15  ...   \n",
              "female                      53            62           62            62  ...   \n",
              "m                           23            34           34            34  ...   \n",
              "male                       154           202          202           202  ...   \n",
              "\n",
              "                Anonymity  Leave  Mental_Health_Consequence  \\\n",
              "Gender                                                        \n",
              "Cis Male                2      2                          2   \n",
              "F                      38     38                         38   \n",
              "Female                121    121                        121   \n",
              "Female                  2      2                          2   \n",
              "Female (trans)          2      2                          2   \n",
              "M                     115    115                        115   \n",
              "Make                    4      4                          4   \n",
              "Male                  611    611                        611   \n",
              "Male                    3      3                          3   \n",
              "Man                     2      2                          2   \n",
              "Woman                   3      3                          3   \n",
              "f                      15     15                         15   \n",
              "female                 62     62                         62   \n",
              "m                      34     34                         34   \n",
              "male                  202    202                        202   \n",
              "\n",
              "                Physical_Health_Consequence  Coworkers  Supervisor  \\\n",
              "Gender                                                               \n",
              "Cis Male                                  2          2           2   \n",
              "F                                        38         38          38   \n",
              "Female                                  121        121         121   \n",
              "Female                                    2          2           2   \n",
              "Female (trans)                            2          2           2   \n",
              "M                                       115        115         115   \n",
              "Make                                      4          4           4   \n",
              "Male                                    611        611         611   \n",
              "Male                                      3          3           3   \n",
              "Man                                       2          2           2   \n",
              "Woman                                     3          3           3   \n",
              "f                                        15         15          15   \n",
              "female                                   62         62          62   \n",
              "m                                        34         34          34   \n",
              "male                                    202        202         202   \n",
              "\n",
              "                Mental_Health_Interview  Physical_Health_Interview  \\\n",
              "Gender                                                               \n",
              "Cis Male                              2                          2   \n",
              "F                                    38                         38   \n",
              "Female                              121                        121   \n",
              "Female                                2                          2   \n",
              "Female (trans)                        2                          2   \n",
              "M                                   115                        115   \n",
              "Make                                  4                          4   \n",
              "Male                                611                        611   \n",
              "Male                                  3                          3   \n",
              "Man                                   2                          2   \n",
              "Woman                                 3                          3   \n",
              "f                                    15                         15   \n",
              "female                               62                         62   \n",
              "m                                    34                         34   \n",
              "male                                202                        202   \n",
              "\n",
              "                Mental_vs_Physical  Obs_Consequence  \n",
              "Gender                                               \n",
              "Cis Male                         2                2  \n",
              "F                               38               38  \n",
              "Female                         121              121  \n",
              "Female                           2                2  \n",
              "Female (trans)                   2                2  \n",
              "M                              115              115  \n",
              "Make                             4                4  \n",
              "Male                           611              611  \n",
              "Male                             3                3  \n",
              "Man                              2                2  \n",
              "Woman                            3                3  \n",
              "f                               15               15  \n",
              "female                          62               62  \n",
              "m                               34               34  \n",
              "male                           202              202  \n",
              "\n",
              "[15 rows x 24 columns]"
            ]
          },
          "execution_count": 214,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.groupby('Gender').count()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fe01abb2",
      "metadata": {
        "id": "fe01abb2",
        "outputId": "fc1dff81-e298-497c-9a0d-627e96cd9e43"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "count",
                  "rawType": "bool",
                  "type": "boolean"
                }
              ],
              "ref": "bf78a1a4-3262-4a29-9d9a-8e76d140832e",
              "rows": [
                [
                  "Male",
                  "False"
                ],
                [
                  "male",
                  "False"
                ],
                [
                  "Female",
                  "False"
                ],
                [
                  "M",
                  "False"
                ],
                [
                  "female",
                  "False"
                ],
                [
                  "F",
                  "False"
                ],
                [
                  "m",
                  "False"
                ],
                [
                  "f",
                  "False"
                ],
                [
                  "Make",
                  "True"
                ],
                [
                  "Woman",
                  "True"
                ],
                [
                  "Male ",
                  "True"
                ],
                [
                  "Cis Male",
                  "True"
                ],
                [
                  "Female ",
                  "True"
                ],
                [
                  "Man",
                  "True"
                ],
                [
                  "Female (trans)",
                  "True"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 15
              }
            },
            "text/plain": [
              "Gender\n",
              "Male              False\n",
              "male              False\n",
              "Female            False\n",
              "M                 False\n",
              "female            False\n",
              "F                 False\n",
              "m                 False\n",
              "f                 False\n",
              "Make               True\n",
              "Woman              True\n",
              "Male               True\n",
              "Cis Male           True\n",
              "Female             True\n",
              "Man                True\n",
              "Female (trans)     True\n",
              "Name: count, dtype: bool"
            ]
          },
          "execution_count": 215,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['Gender'].value_counts()<=10"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "50f2c53d",
      "metadata": {
        "id": "50f2c53d"
      },
      "outputs": [],
      "source": [
        "# remove spaces and lowercase gender column\n",
        "df['Gender'] = df['Gender'].str.strip().str.lower()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f6871917",
      "metadata": {
        "id": "f6871917",
        "outputId": "ee96029a-bb5d-43b6-d6ca-f40c8d8a034a"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Country",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "State",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Self_Employed",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Family_History",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Treatment",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Work_Interfere",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "No_Employees",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Remote_Work",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Tech_Company",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Benefits",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Care_Options",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Wellness_Program",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Seek_Help",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Anonymity",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Leave",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_Health_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Physical_Health_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Coworkers",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Supervisor",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_Health_Interview",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Physical_Health_Interview",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_vs_Physical",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Obs_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "750faeda-f46e-4672-a233-bf973f3b6741",
              "rows": [
                [
                  "cis male",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2"
                ],
                [
                  "f",
                  "53",
                  "53",
                  "45",
                  "53",
                  "53",
                  "53",
                  "44",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53",
                  "53"
                ],
                [
                  "female",
                  "185",
                  "185",
                  "126",
                  "180",
                  "185",
                  "185",
                  "161",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185",
                  "185"
                ],
                [
                  "female (trans)",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2"
                ],
                [
                  "m",
                  "149",
                  "149",
                  "108",
                  "147",
                  "149",
                  "149",
                  "109",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149",
                  "149"
                ],
                [
                  "make",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4"
                ],
                [
                  "male",
                  "816",
                  "816",
                  "430",
                  "805",
                  "816",
                  "816",
                  "636",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816",
                  "816"
                ],
                [
                  "man",
                  "2",
                  "2",
                  "1",
                  "2",
                  "2",
                  "2",
                  "0",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2"
                ],
                [
                  "woman",
                  "3",
                  "3",
                  "2",
                  "3",
                  "3",
                  "3",
                  "1",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3",
                  "3"
                ]
              ],
              "shape": {
                "columns": 24,
                "rows": 9
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>Family_History</th>\n",
              "      <th>Treatment</th>\n",
              "      <th>Work_Interfere</th>\n",
              "      <th>No_Employees</th>\n",
              "      <th>Remote_Work</th>\n",
              "      <th>Tech_Company</th>\n",
              "      <th>...</th>\n",
              "      <th>Anonymity</th>\n",
              "      <th>Leave</th>\n",
              "      <th>Mental_Health_Consequence</th>\n",
              "      <th>Physical_Health_Consequence</th>\n",
              "      <th>Coworkers</th>\n",
              "      <th>Supervisor</th>\n",
              "      <th>Mental_Health_Interview</th>\n",
              "      <th>Physical_Health_Interview</th>\n",
              "      <th>Mental_vs_Physical</th>\n",
              "      <th>Obs_Consequence</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Gender</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>cis male</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>f</th>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>45</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>44</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>...</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "      <td>53</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>female</th>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>126</td>\n",
              "      <td>180</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>161</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>...</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "      <td>185</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>female (trans)</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>m</th>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>108</td>\n",
              "      <td>147</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>109</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>...</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "      <td>149</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>make</th>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>...</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>male</th>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>430</td>\n",
              "      <td>805</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>636</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>...</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "      <td>816</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>man</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>woman</th>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>9 rows × 24 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                Age  Country  State  Self_Employed  Family_History  Treatment  \\\n",
              "Gender                                                                          \n",
              "cis male          2        2      2              2               2          2   \n",
              "f                53       53     45             53              53         53   \n",
              "female          185      185    126            180             185        185   \n",
              "female (trans)    2        2      2              2               2          2   \n",
              "m               149      149    108            147             149        149   \n",
              "make              4        4      4              4               4          4   \n",
              "male            816      816    430            805             816        816   \n",
              "man               2        2      1              2               2          2   \n",
              "woman             3        3      2              3               3          3   \n",
              "\n",
              "                Work_Interfere  No_Employees  Remote_Work  Tech_Company  ...  \\\n",
              "Gender                                                                   ...   \n",
              "cis male                     2             2            2             2  ...   \n",
              "f                           44            53           53            53  ...   \n",
              "female                     161           185          185           185  ...   \n",
              "female (trans)               2             2            2             2  ...   \n",
              "m                          109           149          149           149  ...   \n",
              "make                         4             4            4             4  ...   \n",
              "male                       636           816          816           816  ...   \n",
              "man                          0             2            2             2  ...   \n",
              "woman                        1             3            3             3  ...   \n",
              "\n",
              "                Anonymity  Leave  Mental_Health_Consequence  \\\n",
              "Gender                                                        \n",
              "cis male                2      2                          2   \n",
              "f                      53     53                         53   \n",
              "female                185    185                        185   \n",
              "female (trans)          2      2                          2   \n",
              "m                     149    149                        149   \n",
              "make                    4      4                          4   \n",
              "male                  816    816                        816   \n",
              "man                     2      2                          2   \n",
              "woman                   3      3                          3   \n",
              "\n",
              "                Physical_Health_Consequence  Coworkers  Supervisor  \\\n",
              "Gender                                                               \n",
              "cis male                                  2          2           2   \n",
              "f                                        53         53          53   \n",
              "female                                  185        185         185   \n",
              "female (trans)                            2          2           2   \n",
              "m                                       149        149         149   \n",
              "make                                      4          4           4   \n",
              "male                                    816        816         816   \n",
              "man                                       2          2           2   \n",
              "woman                                     3          3           3   \n",
              "\n",
              "                Mental_Health_Interview  Physical_Health_Interview  \\\n",
              "Gender                                                               \n",
              "cis male                              2                          2   \n",
              "f                                    53                         53   \n",
              "female                              185                        185   \n",
              "female (trans)                        2                          2   \n",
              "m                                   149                        149   \n",
              "make                                  4                          4   \n",
              "male                                816                        816   \n",
              "man                                   2                          2   \n",
              "woman                                 3                          3   \n",
              "\n",
              "                Mental_vs_Physical  Obs_Consequence  \n",
              "Gender                                               \n",
              "cis male                         2                2  \n",
              "f                               53               53  \n",
              "female                         185              185  \n",
              "female (trans)                   2                2  \n",
              "m                              149              149  \n",
              "make                             4                4  \n",
              "male                           816              816  \n",
              "man                              2                2  \n",
              "woman                            3                3  \n",
              "\n",
              "[9 rows x 24 columns]"
            ]
          },
          "execution_count": 217,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.groupby('Gender').count()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "cb6bec2a",
      "metadata": {
        "id": "cb6bec2a"
      },
      "outputs": [],
      "source": [
        "df['Gender'] = df['Gender'].replace({\n",
        "    'male':'M',\n",
        "    'female':'F',\n",
        "    'm':'M',\n",
        "    'f':'F',\n",
        "    'woman':'F',\n",
        "    'man':'M',\n",
        "    'femail':'F',\n",
        "    'mail':'M',\n",
        "    'femake':'F',\n",
        "    'mal':'M',\n",
        "    'mal-ish':'M',\n",
        "    'maile':'M',\n",
        "    'malr':'M',\n",
        "})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "3b20d862",
      "metadata": {
        "id": "3b20d862",
        "outputId": "f486bfc5-596e-430b-bf29-323acfb01bee"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Country",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "State",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Self_Employed",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Family_History",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Treatment",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Work_Interfere",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "No_Employees",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Remote_Work",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Tech_Company",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Benefits",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Care_Options",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Wellness_Program",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Seek_Help",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Anonymity",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Leave",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_Health_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Physical_Health_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Coworkers",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Supervisor",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_Health_Interview",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Physical_Health_Interview",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_vs_Physical",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Obs_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "3b9a586b-9699-434e-9e86-69518e30e160",
              "rows": [
                [
                  "F",
                  "241",
                  "241",
                  "173",
                  "236",
                  "241",
                  "241",
                  "206",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241"
                ],
                [
                  "M",
                  "967",
                  "967",
                  "539",
                  "954",
                  "967",
                  "967",
                  "745",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967"
                ],
                [
                  "cis male",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2"
                ],
                [
                  "female (trans)",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2",
                  "2"
                ],
                [
                  "make",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4",
                  "4"
                ]
              ],
              "shape": {
                "columns": 24,
                "rows": 5
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>Family_History</th>\n",
              "      <th>Treatment</th>\n",
              "      <th>Work_Interfere</th>\n",
              "      <th>No_Employees</th>\n",
              "      <th>Remote_Work</th>\n",
              "      <th>Tech_Company</th>\n",
              "      <th>...</th>\n",
              "      <th>Anonymity</th>\n",
              "      <th>Leave</th>\n",
              "      <th>Mental_Health_Consequence</th>\n",
              "      <th>Physical_Health_Consequence</th>\n",
              "      <th>Coworkers</th>\n",
              "      <th>Supervisor</th>\n",
              "      <th>Mental_Health_Interview</th>\n",
              "      <th>Physical_Health_Interview</th>\n",
              "      <th>Mental_vs_Physical</th>\n",
              "      <th>Obs_Consequence</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Gender</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>F</th>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>173</td>\n",
              "      <td>236</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>206</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>...</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>M</th>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>539</td>\n",
              "      <td>954</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>745</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>...</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>cis male</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>female (trans)</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>make</th>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>...</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 24 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                Age  Country  State  Self_Employed  Family_History  Treatment  \\\n",
              "Gender                                                                          \n",
              "F               241      241    173            236             241        241   \n",
              "M               967      967    539            954             967        967   \n",
              "cis male          2        2      2              2               2          2   \n",
              "female (trans)    2        2      2              2               2          2   \n",
              "make              4        4      4              4               4          4   \n",
              "\n",
              "                Work_Interfere  No_Employees  Remote_Work  Tech_Company  ...  \\\n",
              "Gender                                                                   ...   \n",
              "F                          206           241          241           241  ...   \n",
              "M                          745           967          967           967  ...   \n",
              "cis male                     2             2            2             2  ...   \n",
              "female (trans)               2             2            2             2  ...   \n",
              "make                         4             4            4             4  ...   \n",
              "\n",
              "                Anonymity  Leave  Mental_Health_Consequence  \\\n",
              "Gender                                                        \n",
              "F                     241    241                        241   \n",
              "M                     967    967                        967   \n",
              "cis male                2      2                          2   \n",
              "female (trans)          2      2                          2   \n",
              "make                    4      4                          4   \n",
              "\n",
              "                Physical_Health_Consequence  Coworkers  Supervisor  \\\n",
              "Gender                                                               \n",
              "F                                       241        241         241   \n",
              "M                                       967        967         967   \n",
              "cis male                                  2          2           2   \n",
              "female (trans)                            2          2           2   \n",
              "make                                      4          4           4   \n",
              "\n",
              "                Mental_Health_Interview  Physical_Health_Interview  \\\n",
              "Gender                                                               \n",
              "F                                   241                        241   \n",
              "M                                   967                        967   \n",
              "cis male                              2                          2   \n",
              "female (trans)                        2                          2   \n",
              "make                                  4                          4   \n",
              "\n",
              "                Mental_vs_Physical  Obs_Consequence  \n",
              "Gender                                               \n",
              "F                              241              241  \n",
              "M                              967              967  \n",
              "cis male                         2                2  \n",
              "female (trans)                   2                2  \n",
              "make                             4                4  \n",
              "\n",
              "[5 rows x 24 columns]"
            ]
          },
          "execution_count": 219,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.groupby('Gender').count()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "96e0034c",
      "metadata": {
        "id": "96e0034c"
      },
      "outputs": [],
      "source": [
        "df = df[df['Gender'].isin(['M','F'])]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1a344b06",
      "metadata": {
        "id": "1a344b06",
        "outputId": "a4056edb-ffcb-43a2-d1da-3485362bbf71"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Country",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "State",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Self_Employed",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Family_History",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Treatment",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Work_Interfere",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "No_Employees",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Remote_Work",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Tech_Company",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Benefits",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Care_Options",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Wellness_Program",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Seek_Help",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Anonymity",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Leave",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_Health_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Physical_Health_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Coworkers",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Supervisor",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_Health_Interview",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Physical_Health_Interview",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Mental_vs_Physical",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Obs_Consequence",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "6e665a4e-9fd3-4aff-98d2-33f9f618bafd",
              "rows": [
                [
                  "F",
                  "241",
                  "241",
                  "173",
                  "236",
                  "241",
                  "241",
                  "206",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241",
                  "241"
                ],
                [
                  "M",
                  "967",
                  "967",
                  "539",
                  "954",
                  "967",
                  "967",
                  "745",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967",
                  "967"
                ]
              ],
              "shape": {
                "columns": 24,
                "rows": 2
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>Family_History</th>\n",
              "      <th>Treatment</th>\n",
              "      <th>Work_Interfere</th>\n",
              "      <th>No_Employees</th>\n",
              "      <th>Remote_Work</th>\n",
              "      <th>Tech_Company</th>\n",
              "      <th>...</th>\n",
              "      <th>Anonymity</th>\n",
              "      <th>Leave</th>\n",
              "      <th>Mental_Health_Consequence</th>\n",
              "      <th>Physical_Health_Consequence</th>\n",
              "      <th>Coworkers</th>\n",
              "      <th>Supervisor</th>\n",
              "      <th>Mental_Health_Interview</th>\n",
              "      <th>Physical_Health_Interview</th>\n",
              "      <th>Mental_vs_Physical</th>\n",
              "      <th>Obs_Consequence</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Gender</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>F</th>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>173</td>\n",
              "      <td>236</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>206</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>...</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "      <td>241</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>M</th>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>539</td>\n",
              "      <td>954</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>745</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>...</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "      <td>967</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>2 rows × 24 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "        Age  Country  State  Self_Employed  Family_History  Treatment  \\\n",
              "Gender                                                                  \n",
              "F       241      241    173            236             241        241   \n",
              "M       967      967    539            954             967        967   \n",
              "\n",
              "        Work_Interfere  No_Employees  Remote_Work  Tech_Company  ...  \\\n",
              "Gender                                                           ...   \n",
              "F                  206           241          241           241  ...   \n",
              "M                  745           967          967           967  ...   \n",
              "\n",
              "        Anonymity  Leave  Mental_Health_Consequence  \\\n",
              "Gender                                                \n",
              "F             241    241                        241   \n",
              "M             967    967                        967   \n",
              "\n",
              "        Physical_Health_Consequence  Coworkers  Supervisor  \\\n",
              "Gender                                                       \n",
              "F                               241        241         241   \n",
              "M                               967        967         967   \n",
              "\n",
              "        Mental_Health_Interview  Physical_Health_Interview  \\\n",
              "Gender                                                       \n",
              "F                           241                        241   \n",
              "M                           967                        967   \n",
              "\n",
              "        Mental_vs_Physical  Obs_Consequence  \n",
              "Gender                                       \n",
              "F                      241              241  \n",
              "M                      967              967  \n",
              "\n",
              "[2 rows x 24 columns]"
            ]
          },
          "execution_count": 221,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.groupby('Gender').count()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "5591f64c",
      "metadata": {
        "id": "5591f64c",
        "outputId": "2b8f942b-74d7-42ee-edc1-4078ce26e80a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "Index(['Age', 'Gender', 'Country', 'State', 'Self_Employed', 'Family_History',\n",
              "       'Treatment', 'Work_Interfere', 'No_Employees', 'Remote_Work',\n",
              "       'Tech_Company', 'Benefits', 'Care_Options', 'Wellness_Program',\n",
              "       'Seek_Help', 'Anonymity', 'Leave', 'Mental_Health_Consequence',\n",
              "       'Physical_Health_Consequence', 'Coworkers', 'Supervisor',\n",
              "       'Mental_Health_Interview', 'Physical_Health_Interview',\n",
              "       'Mental_vs_Physical', 'Obs_Consequence'],\n",
              "      dtype='object')"
            ]
          },
          "execution_count": 222,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.columns\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "3b5a581b",
      "metadata": {
        "id": "3b5a581b",
        "outputId": "5415d64b-4622-4ef9-dd2d-cbae20289ef0"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "index",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Age",
                  "rawType": "int64",
                  "type": "integer"
                },
                {
                  "name": "Gender",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Country",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "State",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "Self_Employed",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "Family_History",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Treatment",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Work_Interfere",
                  "rawType": "object",
                  "type": "unknown"
                },
                {
                  "name": "No_Employees",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Remote_Work",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Tech_Company",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Benefits",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Care_Options",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Wellness_Program",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Seek_Help",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Anonymity",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Leave",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Consequence",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Coworkers",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Supervisor",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Physical_Health_Interview",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Mental_vs_Physical",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "Obs_Consequence",
                  "rawType": "object",
                  "type": "string"
                }
              ],
              "ref": "4ab31a82-3a08-4dc0-a720-928651f00752",
              "rows": [
                [
                  "0",
                  "37",
                  "F",
                  "United States",
                  "IL",
                  null,
                  "No",
                  "Yes",
                  "Often",
                  "6-25",
                  "No",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "No",
                  "Yes",
                  "Yes",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "1",
                  "44",
                  "M",
                  "United States",
                  "IN",
                  null,
                  "No",
                  "No",
                  "Rarely",
                  "More than 1000",
                  "No",
                  "No",
                  "Don't know",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "2",
                  "32",
                  "M",
                  "Canada",
                  null,
                  null,
                  "No",
                  "No",
                  "Rarely",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No"
                ],
                [
                  "3",
                  "31",
                  "M",
                  "United Kingdom",
                  null,
                  null,
                  "Yes",
                  "Yes",
                  "Often",
                  "26-100",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "Somewhat difficult",
                  "Yes",
                  "Yes",
                  "Some of them",
                  "No",
                  "Maybe",
                  "Maybe",
                  "No",
                  "Yes"
                ],
                [
                  "4",
                  "31",
                  "M",
                  "United States",
                  "TX",
                  null,
                  "No",
                  "No",
                  "Never",
                  "100-500",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "5",
                  "33",
                  "M",
                  "United States",
                  "TN",
                  null,
                  "Yes",
                  "No",
                  "Sometimes",
                  "6-25",
                  "No",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "6",
                  "35",
                  "F",
                  "United States",
                  "MI",
                  null,
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "1-5",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Somewhat difficult",
                  "Maybe",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "7",
                  "39",
                  "M",
                  "Canada",
                  null,
                  null,
                  "No",
                  "No",
                  "Never",
                  "1-5",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "8",
                  "42",
                  "F",
                  "United States",
                  "IL",
                  null,
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "100-500",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "Very difficult",
                  "Maybe",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "9",
                  "23",
                  "M",
                  "Canada",
                  null,
                  null,
                  "No",
                  "No",
                  "Never",
                  "26-100",
                  "No",
                  "Yes",
                  "Don't know",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "10",
                  "31",
                  "M",
                  "United States",
                  "OH",
                  null,
                  "No",
                  "Yes",
                  "Sometimes",
                  "6-25",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "11",
                  "29",
                  "M",
                  "Bulgaria",
                  null,
                  null,
                  "No",
                  "No",
                  "Never",
                  "100-500",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "12",
                  "42",
                  "F",
                  "United States",
                  "CA",
                  null,
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "No",
                  "Yes"
                ],
                [
                  "13",
                  "36",
                  "M",
                  "United States",
                  "CT",
                  null,
                  "Yes",
                  "No",
                  "Never",
                  "500-1000",
                  "No",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "14",
                  "27",
                  "M",
                  "Canada",
                  null,
                  null,
                  "No",
                  "No",
                  "Never",
                  "6-25",
                  "No",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Some of them",
                  "Maybe",
                  "Yes",
                  "Yes",
                  "No"
                ],
                [
                  "15",
                  "29",
                  "F",
                  "United States",
                  "IL",
                  null,
                  "Yes",
                  "Yes",
                  "Rarely",
                  "26-100",
                  "No",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Yes",
                  "Some of them",
                  "Maybe",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "16",
                  "23",
                  "M",
                  "United Kingdom",
                  null,
                  null,
                  "No",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Very easy",
                  "Maybe",
                  "No",
                  "Some of them",
                  "No",
                  "Maybe",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "17",
                  "32",
                  "M",
                  "United States",
                  "TN",
                  null,
                  "No",
                  "Yes",
                  "Sometimes",
                  "6-25",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "18",
                  "46",
                  "M",
                  "United States",
                  "MD",
                  "Yes",
                  "Yes",
                  "No",
                  "Sometimes",
                  "1-5",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "Yes",
                  "Don't know",
                  "Yes",
                  "Very easy",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes"
                ],
                [
                  "19",
                  "36",
                  "M",
                  "France",
                  null,
                  "Yes",
                  "Yes",
                  "No",
                  null,
                  "6-25",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Some of them",
                  "Maybe",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "20",
                  "29",
                  "M",
                  "United States",
                  "NY",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "100-500",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "Somewhat difficult",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "21",
                  "31",
                  "M",
                  "United States",
                  "NC",
                  "Yes",
                  "No",
                  "No",
                  "Never",
                  "1-5",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Yes",
                  "Somewhat difficult",
                  "No",
                  "No",
                  "Some of them",
                  "Some of them",
                  "No",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "22",
                  "46",
                  "M",
                  "United States",
                  "MA",
                  "No",
                  "No",
                  "Yes",
                  "Often",
                  "26-100",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "23",
                  "41",
                  "M",
                  "United States",
                  "IA",
                  "No",
                  "No",
                  "Yes",
                  "Never",
                  "More than 1000",
                  "No",
                  "No",
                  "Don't know",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "24",
                  "33",
                  "M",
                  "United States",
                  "CA",
                  "No",
                  "Yes",
                  "Yes",
                  "Rarely",
                  "26-100",
                  "No",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "Don't know",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "25",
                  "35",
                  "M",
                  "United States",
                  "TN",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "More than 1000",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "No",
                  "Very easy",
                  "Yes",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No"
                ],
                [
                  "26",
                  "33",
                  "M",
                  "United States",
                  "TN",
                  "No",
                  "No",
                  "No",
                  null,
                  "1-5",
                  "No",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "27",
                  "35",
                  "F",
                  "United States",
                  "CA",
                  "No",
                  "Yes",
                  "Yes",
                  "Rarely",
                  "6-25",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "28",
                  "34",
                  "M",
                  "United States",
                  "OH",
                  "No",
                  "No",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Somewhat difficult",
                  "No",
                  "No",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "29",
                  "37",
                  "M",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "No",
                  "Sometimes",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Very difficult",
                  "Yes",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "30",
                  "32",
                  "M",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "No",
                  "Never",
                  "6-25",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Yes",
                  "Yes",
                  "Some of them",
                  "Some of them",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "31",
                  "31",
                  "M",
                  "United States",
                  "PA",
                  "Yes",
                  "Yes",
                  "No",
                  "Rarely",
                  "1-5",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Yes"
                ],
                [
                  "32",
                  "30",
                  "M",
                  "United Kingdom",
                  null,
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "500-1000",
                  "Yes",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "Yes",
                  "Somewhat easy",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "33",
                  "42",
                  "M",
                  "United States",
                  "WA",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Very easy",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Some of them",
                  "Maybe",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "34",
                  "40",
                  "F",
                  "United States",
                  "WI",
                  "No",
                  "No",
                  "Yes",
                  "Sometimes",
                  "1-5",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "Some of them",
                  "No",
                  "No",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "35",
                  "27",
                  "M",
                  "United States",
                  "NY",
                  "No",
                  "No",
                  "Yes",
                  "Rarely",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Very easy",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "36",
                  "29",
                  "M",
                  "Canada",
                  null,
                  "No",
                  "No",
                  "No",
                  "Rarely",
                  "1-5",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Very easy",
                  "Yes",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ],
                [
                  "37",
                  "38",
                  "M",
                  "Portugal",
                  null,
                  "No",
                  "No",
                  "No",
                  null,
                  "100-500",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat easy",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Some of them",
                  "No",
                  "Maybe",
                  "No",
                  "No"
                ],
                [
                  "38",
                  "50",
                  "M",
                  "United States",
                  "IN",
                  "No",
                  "No",
                  "No",
                  null,
                  "100-500",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "39",
                  "35",
                  "M",
                  "United States",
                  "TX",
                  "No",
                  "No",
                  "Yes",
                  "Rarely",
                  "More than 1000",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "Very easy",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Maybe",
                  "Yes",
                  "No"
                ],
                [
                  "40",
                  "24",
                  "M",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "Yes",
                  "Sometimes",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "Maybe",
                  "Some of them",
                  "No",
                  "No",
                  "Yes",
                  "No",
                  "Yes"
                ],
                [
                  "41",
                  "35",
                  "M",
                  "United States",
                  "MI",
                  "No",
                  "No",
                  "No",
                  null,
                  "More than 1000",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Not sure",
                  "Don't know",
                  "Yes",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "Yes",
                  "Some of them",
                  "No",
                  "No",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "42",
                  "27",
                  "M",
                  "Canada",
                  null,
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "1-5",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "Very difficult",
                  "Maybe",
                  "No",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "Yes",
                  "No"
                ],
                [
                  "43",
                  "18",
                  "M",
                  "Netherlands",
                  null,
                  "No",
                  "No",
                  "No",
                  "Often",
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "Not sure",
                  "No",
                  "No",
                  "Don't know",
                  "Somewhat difficult",
                  "Yes",
                  "Maybe",
                  "No",
                  "Some of them",
                  "No",
                  "No",
                  "No",
                  "No"
                ],
                [
                  "44",
                  "30",
                  "M",
                  "United States",
                  "IN",
                  "No",
                  "No",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "No",
                  "Yes",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Maybe",
                  "Don't know",
                  "No"
                ],
                [
                  "45",
                  "38",
                  "F",
                  "United States",
                  "TX",
                  "No",
                  "Yes",
                  "Yes",
                  "Sometimes",
                  "26-100",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "Somewhat easy",
                  "No",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "No"
                ],
                [
                  "46",
                  "28",
                  "M",
                  "United Kingdom",
                  null,
                  "No",
                  "No",
                  "No",
                  null,
                  "26-100",
                  "No",
                  "Yes",
                  "Don't know",
                  "Not sure",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "Maybe",
                  "Some of them",
                  "Yes",
                  "Maybe",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "47",
                  "34",
                  "M",
                  "United States",
                  "TN",
                  "No",
                  "No",
                  "No",
                  null,
                  "6-25",
                  "No",
                  "Yes",
                  "No",
                  "No",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "Maybe",
                  "Yes",
                  "Don't know",
                  "No"
                ],
                [
                  "48",
                  "26",
                  "M",
                  "Canada",
                  null,
                  "Yes",
                  "No",
                  "No",
                  "Sometimes",
                  "1-5",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "Don't know",
                  "Don't know",
                  "No",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Yes",
                  "No"
                ],
                [
                  "49",
                  "30",
                  "M",
                  "United States",
                  "IL",
                  "No",
                  "Yes",
                  "Yes",
                  "Rarely",
                  "26-100",
                  "No",
                  "Yes",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "Don't know",
                  "Don't know",
                  "Maybe",
                  "No",
                  "Some of them",
                  "Yes",
                  "No",
                  "No",
                  "Don't know",
                  "No"
                ]
              ],
              "shape": {
                "columns": 25,
                "rows": 1208
              }
            },
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Age</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Country</th>\n",
              "      <th>State</th>\n",
              "      <th>Self_Employed</th>\n",
              "      <th>Family_History</th>\n",
              "      <th>Treatment</th>\n",
              "      <th>Work_Interfere</th>\n",
              "      <th>No_Employees</th>\n",
              "      <th>Remote_Work</th>\n",
              "      <th>...</th>\n",
              "      <th>Anonymity</th>\n",
              "      <th>Leave</th>\n",
              "      <th>Mental_Health_Consequence</th>\n",
              "      <th>Physical_Health_Consequence</th>\n",
              "      <th>Coworkers</th>\n",
              "      <th>Supervisor</th>\n",
              "      <th>Mental_Health_Interview</th>\n",
              "      <th>Physical_Health_Interview</th>\n",
              "      <th>Mental_vs_Physical</th>\n",
              "      <th>Obs_Consequence</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>37</td>\n",
              "      <td>F</td>\n",
              "      <td>United States</td>\n",
              "      <td>IL</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>6-25</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Somewhat easy</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>44</td>\n",
              "      <td>M</td>\n",
              "      <td>United States</td>\n",
              "      <td>IN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Rarely</td>\n",
              "      <td>More than 1000</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>32</td>\n",
              "      <td>M</td>\n",
              "      <td>Canada</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Rarely</td>\n",
              "      <td>6-25</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>31</td>\n",
              "      <td>M</td>\n",
              "      <td>United Kingdom</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>26-100</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>No</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>No</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>31</td>\n",
              "      <td>M</td>\n",
              "      <td>United States</td>\n",
              "      <td>TX</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Never</td>\n",
              "      <td>100-500</td>\n",
              "      <td>Yes</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1254</th>\n",
              "      <td>26</td>\n",
              "      <td>M</td>\n",
              "      <td>United Kingdom</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>NaN</td>\n",
              "      <td>26-100</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Somewhat easy</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1255</th>\n",
              "      <td>32</td>\n",
              "      <td>M</td>\n",
              "      <td>United States</td>\n",
              "      <td>IL</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Often</td>\n",
              "      <td>26-100</td>\n",
              "      <td>Yes</td>\n",
              "      <td>...</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1256</th>\n",
              "      <td>34</td>\n",
              "      <td>M</td>\n",
              "      <td>United States</td>\n",
              "      <td>CA</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Sometimes</td>\n",
              "      <td>More than 1000</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Somewhat difficult</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1257</th>\n",
              "      <td>46</td>\n",
              "      <td>F</td>\n",
              "      <td>United States</td>\n",
              "      <td>NC</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>NaN</td>\n",
              "      <td>100-500</td>\n",
              "      <td>Yes</td>\n",
              "      <td>...</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1258</th>\n",
              "      <td>25</td>\n",
              "      <td>M</td>\n",
              "      <td>United States</td>\n",
              "      <td>IL</td>\n",
              "      <td>No</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Sometimes</td>\n",
              "      <td>26-100</td>\n",
              "      <td>No</td>\n",
              "      <td>...</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>Maybe</td>\n",
              "      <td>No</td>\n",
              "      <td>Some of them</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>Don't know</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1208 rows × 25 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      Age Gender         Country State Self_Employed Family_History Treatment  \\\n",
              "0      37      F   United States    IL           NaN             No       Yes   \n",
              "1      44      M   United States    IN           NaN             No        No   \n",
              "2      32      M          Canada   NaN           NaN             No        No   \n",
              "3      31      M  United Kingdom   NaN           NaN            Yes       Yes   \n",
              "4      31      M   United States    TX           NaN             No        No   \n",
              "...   ...    ...             ...   ...           ...            ...       ...   \n",
              "1254   26      M  United Kingdom   NaN            No             No       Yes   \n",
              "1255   32      M   United States    IL            No            Yes       Yes   \n",
              "1256   34      M   United States    CA            No            Yes       Yes   \n",
              "1257   46      F   United States    NC            No             No        No   \n",
              "1258   25      M   United States    IL            No            Yes       Yes   \n",
              "\n",
              "     Work_Interfere    No_Employees Remote_Work  ...   Anonymity  \\\n",
              "0             Often            6-25          No  ...         Yes   \n",
              "1            Rarely  More than 1000          No  ...  Don't know   \n",
              "2            Rarely            6-25          No  ...  Don't know   \n",
              "3             Often          26-100          No  ...          No   \n",
              "4             Never         100-500         Yes  ...  Don't know   \n",
              "...             ...             ...         ...  ...         ...   \n",
              "1254            NaN          26-100          No  ...  Don't know   \n",
              "1255          Often          26-100         Yes  ...         Yes   \n",
              "1256      Sometimes  More than 1000          No  ...  Don't know   \n",
              "1257            NaN         100-500         Yes  ...  Don't know   \n",
              "1258      Sometimes          26-100          No  ...         Yes   \n",
              "\n",
              "                   Leave Mental_Health_Consequence  \\\n",
              "0          Somewhat easy                        No   \n",
              "1             Don't know                     Maybe   \n",
              "2     Somewhat difficult                        No   \n",
              "3     Somewhat difficult                       Yes   \n",
              "4             Don't know                        No   \n",
              "...                  ...                       ...   \n",
              "1254       Somewhat easy                        No   \n",
              "1255  Somewhat difficult                        No   \n",
              "1256  Somewhat difficult                       Yes   \n",
              "1257          Don't know                       Yes   \n",
              "1258          Don't know                     Maybe   \n",
              "\n",
              "     Physical_Health_Consequence     Coworkers    Supervisor  \\\n",
              "0                             No  Some of them           Yes   \n",
              "1                             No            No            No   \n",
              "2                             No           Yes           Yes   \n",
              "3                            Yes  Some of them            No   \n",
              "4                             No  Some of them           Yes   \n",
              "...                          ...           ...           ...   \n",
              "1254                          No  Some of them  Some of them   \n",
              "1255                          No  Some of them           Yes   \n",
              "1256                         Yes            No            No   \n",
              "1257                          No            No            No   \n",
              "1258                          No  Some of them            No   \n",
              "\n",
              "     Mental_Health_Interview Physical_Health_Interview Mental_vs_Physical  \\\n",
              "0                         No                     Maybe                Yes   \n",
              "1                         No                        No         Don't know   \n",
              "2                        Yes                       Yes                 No   \n",
              "3                      Maybe                     Maybe                 No   \n",
              "4                        Yes                       Yes         Don't know   \n",
              "...                      ...                       ...                ...   \n",
              "1254                      No                        No         Don't know   \n",
              "1255                      No                        No                Yes   \n",
              "1256                      No                        No                 No   \n",
              "1257                      No                        No                 No   \n",
              "1258                      No                        No         Don't know   \n",
              "\n",
              "     Obs_Consequence  \n",
              "0                 No  \n",
              "1                 No  \n",
              "2                 No  \n",
              "3                Yes  \n",
              "4                 No  \n",
              "...              ...  \n",
              "1254              No  \n",
              "1255              No  \n",
              "1256              No  \n",
              "1257              No  \n",
              "1258              No  \n",
              "\n",
              "[1208 rows x 25 columns]"
            ]
          },
          "execution_count": 225,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1d163919",
      "metadata": {
        "id": "1d163919",
        "outputId": "d5cfd30c-8abe-4e92-fd8f-5a5afc9cd026"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "np.int64(712)"
            ]
          },
          "execution_count": 229,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['State'].value_counts().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f6931101",
      "metadata": {
        "id": "f6931101"
      },
      "outputs": [],
      "source": [
        "df.drop(labels='State', axis=1, inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "88b2a4cd",
      "metadata": {
        "id": "88b2a4cd"
      },
      "outputs": [],
      "source": [
        "df.dropna(subset=['Self_Employed'], inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "46311d39",
      "metadata": {
        "id": "46311d39"
      },
      "outputs": [],
      "source": [
        "df.replace(\"Don't know\",\"No\", inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "86cda8ed",
      "metadata": {
        "id": "86cda8ed",
        "outputId": "49fad471-07f2-4464-9c1c-6fae1f170ba7"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.microsoft.datawrangler.viewer.v0+json": {
              "columns": [
                {
                  "name": "Leave",
                  "rawType": "object",
                  "type": "string"
                },
                {
                  "name": "count",
                  "rawType": "int64",
                  "type": "integer"
                }
              ],
              "ref": "fba538a1-e697-4d7d-a95f-81ceef8b27a8",
              "rows": [
                [
                  "No",
                  "539"
                ],
                [
                  "Somewhat easy",
                  "250"
                ],
                [
                  "Very easy",
                  "198"
                ],
                [
                  "Somewhat difficult",
                  "112"
                ],
                [
                  "Very difficult",
                  "91"
                ]
              ],
              "shape": {
                "columns": 1,
                "rows": 5
              }
            },
            "text/plain": [
              "Leave\n",
              "No                    539\n",
              "Somewhat easy         250\n",
              "Very easy             198\n",
              "Somewhat difficult    112\n",
              "Very difficult         91\n",
              "Name: count, dtype: int64"
            ]
          },
          "execution_count": 236,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df['Leave'].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "bc7595dc",
      "metadata": {
        "id": "bc7595dc"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "mental-health-survey",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.14.0"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}