FROM torizon/debian:stable-rc AS base
ARG BUILD_CONFIGURATION=Release
WORKDIR /app

FROM base AS build
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
        python3 \
        libusb-1.0-0 \
	    # Check which packages are included in your base image \
	    # Add additional packages here if required for the build process \
	    # If no packages are required, this step is automatically skipped \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/oceandirect/apt/lists/*

# Copy source files in layers to take advantage of caching
COPY *.py ./src/

# Copy any remaining dependencies
COPY ./ ./src/

ENTRYPOINT ["python3", "src/main.py"]