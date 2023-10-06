from esbill import app, runner

if __name__ == "__main__":
    import uvicorn
    import os
    import logging

    logging.basicConfig(level=logging.DEBUG)

    os.environ['PERSISTENCE_MODULE'] = 'eventsourcing.sqlite'
    os.environ['SQLITE_DBNAME'] = ':memory:'

    try:
        runner.start()
        uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="debug")
    except:
        runner.stop()
