import os
import sys
import snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def run_sql_file(sql_file_path):
    """
    Connects to Snowflake using environment variables and executes a SQL file.
    """
    try:
        # Retrieve credentials from environment variables
        account = os.environ.get('SNOWSQL_ACCOUNT')
        database = os.environ.get('SNOWSQL_DATABASE')
        private_key_pem = os.environ.get('SNOWSQL_PRIVATE_KEY')
        role = os.environ.get('SNOWSQL_ROLE')
        schema = os.environ.get('SNOWSQL_SCHEMA')
        user = os.environ.get('SNOWSQL_USER')
        warehouse = os.environ.get('SNOWSQL_WAREHOUSE')

        # Validate that all required environment variables are set
        if not all([account, database, private_key_pem, role, schema, user, warehouse]):
            raise ValueError("One or more Snowflake environment variables are not set.")

        # Load the private key
        # Assuming the private key is provided as a PEM string in the secret
        # If your private key requires a passphrase, you'll need to handle it here.
        # For simplicity, this example assumes no passphrase.
        p_key = serialization.load_pem_private_key(
            private_key_pem.encode('utf-8'),
            password=None, # Replace with your passphrase if applicable, or get from another secret
            backend=default_backend()
        )

        # Connect to Snowflake
        print(f"Connecting to Snowflake account: {account} as user: {user}...")
        conn = snowflake.connector.connect(
            user=user,
            account=account,
            private_key=p_key,
            warehouse=warehouse,
            database=database,
            schema=schema,
            role=role
        )
        print("Successfully connected to Snowflake.")

        # Read SQL from file
        with open(sql_file_path, 'r') as f:
            sql_commands = f.read()

        # Execute SQL commands
        cursor = conn.cursor()
        print(f"Executing SQL from: {sql_file_path}")
        # Snowflake connector can execute multiple statements separated by semicolons
        # However, for complex scripts, it's often safer to split them and execute
        # one by one if there are issues with multi-statement execution.
        # For simple cases, this should work.
        for command in sql_commands.split(';'):
            if command.strip(): # Only execute non-empty commands
                try:
                    cursor.execute(command)
                    # If you expect results, you can fetch them here:
                    # for row in cursor:
                    #     print(row)
                    print(f"Command executed successfully: {command.strip()[:50]}...")
                except Exception as e:
                    print(f"Error executing command: {command.strip()[:50]}...")
                    print(f"Error: {e}")
                    raise # Re-raise to fail the workflow

        print("All SQL commands executed successfully.")

    except ValueError as ve:
        print(f"Configuration Error: {ve}")
        sys.exit(1) # Exit with error code
    except FileNotFoundError:
        print(f"Error: SQL file not found at {sql_file_path}")
        sys.exit(1)
    except snowflake.connector.errors.ProgrammingError as pe:
        print(f"Snowflake Programming Error: {pe}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Snowflake connection closed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_snowflake_sql.py <sql_file_path>")
        sys.exit(1)
    sql_file = sys.argv[1]
    run_sql_file(sql_file)
