import subprocess

result = subprocess.run(
    ['psql', '-h', 'localhost', '-U', 'odoo', '-d', 'odoo19', '-c', '\\dt'],
    input='1234\n',
    capture_output=True,
    text=True
)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)