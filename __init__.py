from workspace.applications.engine import Process

if __name__ == "__main__":
    process = Process()
    process.run(debug = True, port = 5100)