# Logging Mechanisms in EcoCode

EcoCode uses a robust logging system to track application events, errors, and performance metrics. This document outlines the logging mechanisms and best practices for using and extending the logging functionality.

## Overview

The logging system is implemented using Python's built-in `logging` module, configured to capture various levels of logs such as:

- **DEBUG**: Detailed information, useful for debugging.
- **INFO**: General application information.
- **WARNING**: Indications of potential problems.
- **ERROR**: Errors that occur during execution.
- **CRITICAL**: Severe errors causing application shutdown.

Logs can be output to the console, log files, or external monitoring tools.

## Default Configuration

The default logging configuration is defined in `logger.py`:

- Log level: `INFO`
- Log format: `[%(asctime)s] %(levelname)s - %(message)s`
- Output: Logs are written to both the console and a rotating file `ecocode.log`.

### Example of Default Logging

```python
import logging
from ecocode.logger import configure_logging

# Configure the logger
logger = configure_logging()

logger.info("EcoCode started successfully.")
logger.error("An error occurred while analyzing energy impact.")
```

## File Structure

Logs are stored in the `logs/` directory with a rotating file handler:

- `ecocode.log`: Contains the most recent logs.
- `ecocode.log.1`, `ecocode.log.2`, etc.: Archived log files.

## Customizing Logging

Developers can customize the logging system to suit their needs. The following parameters can be modified:

1. **Log Level**: Adjust the verbosity of logs (e.g., `DEBUG` for development).
2. **Log Format**: Change the format to include additional information.
3. **Output Handlers**: Add handlers for external monitoring tools (e.g., Syslog, Cloudwatch).

### Example of Custom Configuration

```python
import logging

# Custom logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("custom.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("CustomLogger")
logger.debug("This is a debug message.")
```

## Best Practices

1. Use appropriate log levels to avoid noise in production environments.
2. Avoid logging sensitive data (e.g., passwords, personal information).
3. Regularly monitor log files for issues and performance bottlenecks.
4. Rotate and archive logs to prevent storage overflow.

## Extending Logging

To integrate with third-party tools, create a custom handler:

```python
from logging import Handler

class CustomHandler(Handler):
    def emit(self, record):
        # Custom logic for handling logs
        pass

# Add the custom handler to the logger
logger.addHandler(CustomHandler())
```

## Troubleshooting

If logging does not work as expected:

1. Verify the `logging` configuration in `logger.py`.
2. Check file permissions for the `logs/` directory.
3. Ensure sufficient disk space for log files.
