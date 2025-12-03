"""
Taiwan Election Prediction - Data Cleaning Script
Integrates election, revenue, population structure, and education data
"""

import pandas as pd
import numpy as np
import warnings
import sys
import io

# Set UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

warnings.filterwarnings('ignore')

def clean_vote_data(file_path):
    """Clean election data"""
    print("\n" + "="*60)
    print("Step 1: Cleaning Election Data")
    print("="*60)

    df = pd.read_csv(file_path)

    # Simplify column names
    df.columns = ['District', 'Ko_Wu', 'Lai_Hsiao', 'Hou_Chao']

    # Clean numbers 
    for col in ['Ko_Wu', 'Lai_Hsiao', 'Hou_Chao']:
        df[col] = df[col].astype(str).str.replace(',', '').str.strip()
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove empty rows
    df = df.dropna(subset=['Ko_Wu', 'Lai_Hsiao', 'Hou_Chao'])

    # Calculate total votes and percentages
    df['Total_Votes'] = df['Ko_Wu'] + df['Lai_Hsiao'] + df['Hou_Chao']
    df['Ko_Wu_Pct'] = (df['Ko_Wu'] / df['Total_Votes'] * 100).round(2)
    df['Lai_Hsiao_Pct'] = (df['Lai_Hsiao'] / df['Total_Votes'] * 100).round(2)
    df['Hou_Chao_Pct'] = (df['Hou_Chao'] / df['Total_Votes'] * 100).round(2)

    # Determine winner
    def winner(row):
        max_votes = max(row['Ko_Wu'], row['Lai_Hsiao'], row['Hou_Chao'])
        if row['Ko_Wu'] == max_votes:
            return 'Ko_Wu'
        elif row['Lai_Hsiao'] == max_votes:
            return 'Lai_Hsiao'
        else:
            return 'Hou_Chao'

    df['Winner'] = df.apply(winner, axis=1)

    print(f"Election data cleaned: {len(df)} districts")
    print(f"  - Total votes: {df['Total_Votes'].sum():,.0f}")
    print(f"  - Lai-Hsiao: {df['Lai_Hsiao'].sum()/df['Total_Votes'].sum()*100:.2f}%")
    print(f"  - Hou-Chao: {df['Hou_Chao'].sum()/df['Total_Votes'].sum()*100:.2f}%")
    print(f"  - Ko-Wu: {df['Ko_Wu'].sum()/df['Total_Votes'].sum()*100:.2f}%")

    return df

def clean_population_data(file_path):
    """Clean population structure data"""
    print("\n" + "="*60)
    print("Step 2: Cleaning Population Structure Data")
    print("="*60)

    df = pd.read_csv(file_path, encoding='utf-8-sig')

    # Remove total row
    df = df[df['District'].notna()]
    df = df[~df['District'].str.contains('Total', na=False, case=False)]

    # Clean numbers 
    for col in df.columns[1:]:
        df[col] = df[col].astype(str).str.replace(',', '').str.strip()
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Rename columns
    df = df.rename(columns={
        '0-14 years old': 'Age_0_14',
        '15-64 years old': 'Age_15_64',
        'above 65 years old': 'Age_65_Plus'
    })

    # Calculate total population
    df['Total_Population'] = df['Age_0_14'] + df['Age_15_64'] + df['Age_65_Plus']

    # Calculate percentages
    df['Age_0_14_Pct'] = (df['Age_0_14'] / df['Total_Population'] * 100).round(2)
    df['Age_15_64_Pct'] = (df['Age_15_64'] / df['Total_Population'] * 100).round(2)
    df['Age_65_Plus_Pct'] = (df['Age_65_Plus'] / df['Total_Population'] * 100).round(2)

    print(f"Population data cleaned: {len(df)} districts")
    print(f"  - Total population: {df['Total_Population'].sum():,.0f}")
    print(f"  - Avg elderly (65+): {df['Age_65_Plus_Pct'].mean():.2f}%")
    print(f"  - Avg elderly (15-64): {df['Age_15_64_Pct'].mean():.2f}%")
    print(f"  - Avg youth (0-14): {df['Age_0_14_Pct'].mean():.2f}%")

    return df

def clean_revenue_data(file_path):
    """Clean revenue data"""
    print("\n" + "="*60)
    print("Step 3: Cleaning Revenue Data")
    print("="*60)

    df = pd.read_csv(file_path, encoding='utf-8-sig')

    # Rename columns
    df = df.rename(columns={
        'City': 'District',
        'Average people per household': 'Avg_People_Per_HH',
        'Disposable income': 'Disposable_Income',
        'Consumption expenditure': 'Consumption'
    })

    # Select key columns
    key_columns = ['District', 'Households', 'Avg_People_Per_HH',
                   'Income', 'Disposable_Income', 'Consumption']
    df = df[key_columns]

    print(f"[Revenue data cleaned: {len(df)} districts")
    print(f"  - Avg income: {df['Income'].mean():,.0f} TWD")
    print(f"  - Avg disposable income: {df['Disposable_Income'].mean():,.0f} TWD")
    print(f" Missing: Kinmen, Lienchiang")

    return df

def clean_education_data(file_path):
    """Clean education data"""
    print("\n" + "="*60)
    print("Step 4: Cleaning Education Data")
    print("="*60)

    df = pd.read_csv(file_path)

    # Remove empty rows
    df = df.dropna(subset=['District'])

    # Calculate total population (15+)
    edu_columns = ['illiterate or selfstudy', 'edu_primary', 'edu_junior',
                   'edu_highschool', 'edu_junior_college', 'edu_college', 'edu_graudate']

    df['Total_15Plus'] = df[edu_columns].sum(axis=1)

    # Calculate education percentages
    df['Illiterate_Pct'] = (df['illiterate or selfstudy'] / df['Total_15Plus'] * 100).round(2)
    df['Primary_Pct'] = (df['edu_primary'] / df['Total_15Plus'] * 100).round(2)
    df['Junior_Pct'] = (df['edu_junior'] / df['Total_15Plus'] * 100).round(2)
    df['HighSchool_Pct'] = (df['edu_highschool'] / df['Total_15Plus'] * 100).round(2)
    df['JuniorCollege_Pct'] = (df['edu_junior_college'] / df['Total_15Plus'] * 100).round(2)
    df['College_Pct'] = (df['edu_college'] / df['Total_15Plus'] * 100).round(2)
    df['Graduate_Pct'] = (df['edu_graudate'] / df['Total_15Plus'] * 100).round(2)

    # Calculate higher education percentage 
    df['Higher_Education_Pct'] = (
        (df['edu_junior_college'] + df['edu_college'] + df['edu_graudate']) /
        df['Total_15Plus'] * 100
    ).round(2)

    # Select key columns
    key_columns = ['District', 'Total_15Plus', 'Higher_Education_Pct',
                   'Illiterate_Pct', 'Primary_Pct', 'Junior_Pct',
                   'HighSchool_Pct', 'JuniorCollege_Pct', 'College_Pct', 'Graduate_Pct']

    df = df[key_columns]

    print(f"Education data cleaned: {len(df)} districts")
    print(f"  - Avg higher education: {df['Higher_Education_Pct'].mean():.2f}%")
    print(f"  - Highest: {df.loc[df['Higher_Education_Pct'].idxmax(), 'District']} ({df['Higher_Education_Pct'].max():.2f}%)")
    print(f"  - Lowest: {df.loc[df['Higher_Education_Pct'].idxmin(), 'District']} ({df['Higher_Education_Pct'].min():.2f}%)")

    return df

def merge_all_data(vote_df, population_df, revenue_df, education_df,
                   exclude_districts=['Kinmen County', 'Lienchiang County']):
    """Merge all data"""
    print("\n" + "="*60)
    print("Step 5: Merging All Data")
    print("="*60)

    # Merge election and population data
    merged_df = vote_df.merge(
        population_df,
        on='District',
        how='left'
    )

    # Merge revenue data (inner join to exclude Kinmen, Lienchiang)
    merged_df = merged_df.merge(
        revenue_df,
        on='District',
        how='inner'
    )

    # Merge education data
    merged_df = merged_df.merge(
        education_df,
        on='District',
        how='left'
    )

    # Reorder columns 
    cols_order = [
        'District', 'Winner',
        # Election results
        'Total_Votes', 'Ko_Wu', 'Ko_Wu_Pct',
        'Lai_Hsiao', 'Lai_Hsiao_Pct',
        'Hou_Chao', 'Hou_Chao_Pct',
        # Population structure
        'Total_Population', 'Age_0_14', 'Age_0_14_Pct',
        'Age_15_64', 'Age_15_64_Pct',
        'Age_65_Plus', 'Age_65_Plus_Pct',
        # Economic indicators
        'Income', 'Disposable_Income', 'Consumption',
        'Households', 'Avg_People_Per_HH',
        # Education levels
        'Total_15Plus', 'Higher_Education_Pct',
        'Graduate_Pct', 'College_Pct', 'JuniorCollege_Pct',
        'HighSchool_Pct', 'Junior_Pct', 'Primary_Pct', 'Illiterate_Pct'
    ]

    # Keep existing columns
    cols_order = [col for col in cols_order if col in merged_df.columns]
    merged_df = merged_df[cols_order]

    print(f"\n Data merged: {len(merged_df)} districts")
    print(f"  Total columns: {len(merged_df.columns)}")

    # Check missing values
    print(f"\n Missing value check:")
    missing = merged_df.isnull().sum()
    if missing.sum() == 0:
        print("No missing values")
    else:
        print("Found missing values:")
        for col, count in missing[missing > 0].items():
            print(f"    - {col}: {count}")

    # Excluded districts explanation
    excluded = vote_df[vote_df['District'].isin(exclude_districts)]
    if len(excluded) > 0:
        print(f"\nExcluded districts (revenue data missing):")
        for _, row in excluded.iterrows():
            pct = row['Total_Votes'] / vote_df['Total_Votes'].sum() * 100
            print(f"  - {row['District']}: {row['Total_Votes']:,} votes ({pct:.3f}%)")

    return merged_df

def generate_summary_stats(df):
    """Generate summary statistics"""
    print("\n" + "="*60)
    print("Data Summary Statistics")
    print("="*60)

    print(f"\n[Election Results]")
    print(f"  - Lai-Hsiao wins: {(df['Winner'] == 'Lai_Hsiao').sum()} districts")
    print(f"  - Hou-Chao wins: {(df['Winner'] == 'Hou_Chao').sum()} districts")
    print(f"  - Ko-Wu wins: {(df['Winner'] == 'Ko_Wu').sum()} districts")

    print(f"\n[Population Structure]")
    print(f"  - Avg elderly (65+): {df['Age_65_Plus_Pct'].mean():.2f}%")
    print(f"  - Avg youth (0-14): {df['Age_0_14_Pct'].mean():.2f}%")
    print(f"  - Avg working age (15-64): {df['Age_15_64_Pct'].mean():.2f}%")

    print(f"\n[Economic Indicators]")
    print(f"  - Avg income: {df['Income'].mean():,.0f} TWD")
    print(f"  - Avg disposable income: {df['Disposable_Income'].mean():,.0f} TWD")
    print(f"  - Income std dev: {df['Income'].std():,.0f} TWD")

    print(f"\n[Education Level]")
    print(f"  - Avg higher education: {df['Higher_Education_Pct'].mean():.2f}%")
    print(f"  - Avg graduate degree: {df['Graduate_Pct'].mean():.2f}%")

def main():
    print("\n" + "="*70)
    print("Taiwan Election Prediction - Data Cleaning and Integration")
    print("="*70)

    # Set paths
    base_path = r"C:\Users\4019-tjyen\Desktop\Taiwan_election_prediction\data"

    # Clean each dataset
    vote_df = clean_vote_data(f"{base_path}/vote.csv")
    population_df = clean_population_data(f"{base_path}/population_structure_Jan.csv")
    revenue_df = clean_revenue_data(f"{base_path}/revenue.csv")
    education_df = clean_education_data(f"{base_path}/education.csv")

    # Merge data
    final_df = merge_all_data(vote_df, population_df, revenue_df, education_df)

    # Save results
    output_path = f"{base_path}/processed/cleaned_data.csv"
    final_df.to_csv(output_path, index=False, encoding='utf-8-sig')

    print("\n" + "="*70)
    print("Data Cleaning Complete!")
    print("="*70)
    print(f"Cleaned data saved to:")
    print(f"{output_path}")

    # Generate summary statistics
    generate_summary_stats(final_df)

    # Display first few rows
    print("\n" + "="*70)
    print("First 5 Rows Preview")
    print("="*70)
    print(final_df.head().to_string())

    print("\n" + "="*70)
    print("[Data cleaning is completed.")
    print("="*70)

    return final_df

if __name__ == "__main__":
    df = main()
