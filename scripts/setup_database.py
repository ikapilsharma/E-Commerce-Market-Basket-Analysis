#!/usr/bin/env python3
"""
Setup database for GitHub Codespaces
"""

import subprocess
import sys
import os

def run_sql_file(sql_file):
    """Run SQL file against PostgreSQL"""
    try:
        # Set up database
        subprocess.run([
            'psql', 
            '-U', 'postgres', 
            '-d', 'postgres',
            '-c', f"CREATE DATABASE mba_db;"
        ], check=True)
        
        # Run the SQL file
        with open(sql_file, 'r') as f:
            sql_content = f.read()
        
        subprocess.run([
            'psql', 
            '-U', 'postgres', 
            '-d', 'mba_db',
            '-c', sql_content
        ], check=True)
        
        print(f"✅ Successfully ran {sql_file}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {sql_file}: {e}")
        return False

def main():
    print("🚀 Setting up database for GitHub Codespaces...")
    
    # Check if we're in Codespaces
    if os.getenv('CODESPACES'):
        print("✅ Running in GitHub Codespaces")
        
        # Run database setup
        sql_file = 'scripts/create_tables.sql'
        if os.path.exists(sql_file):
            if run_sql_file(sql_file):
                print("✅ Database setup complete!")
                print("🌐 Your app will be available at: https://your-codespace-5003.preview.app.github.dev")
            else:
                print("❌ Database setup failed")
        else:
            print(f"❌ SQL file not found: {sql_file}")
    else:
        print("ℹ️  Not running in Codespaces, skipping database setup")

if __name__ == "__main__":
    main()
