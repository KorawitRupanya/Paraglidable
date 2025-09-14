# Use NVIDIA's TensorFlow L4T image for Jetson (ARM64)
FROM nvcr.io/nvidia/l4t-tensorflow:r8.9.0-tf2.14-py3

# Arguments
ARG USERNAME=paraglidable

# Create a non-root user
RUN useradd -m $USERNAME \
    && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set environment
ENV HOME=/home/$USERNAME
ENV DEBIAN_FRONTEND=noninteractive
ENV NPY_DISABLE_CPU_FEATURES=AVX,AVX2,FMA

# Set working directory
WORKDIR $HOME
USER $USERNAME

# Upgrade pip
RUN pip install --upgrade pip

# Install system dependencies (sudo needed since we are non-root)
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    net-tools \
    libopenjp2-7-dev \
    libpng-dev \
    libpng16-16 \
    vim \
    sass \
    wget \
    qt5-default \
    pdf2svg \
    apache2 \
    php \
    libapache2-mod-php \
    nodejs \
    npm \
    libgrib-api-dev \
    unzip \
    sudo \
    libgeos-dev \
    libproj-dev \
    && rm -rf /var/lib/apt/lists/*

# Return to non-root user
USER $USERNAME
WORKDIR $HOME

# Install basemap 1.2.1 from GitHub tarball
RUN pip install --no-cache-dir https://github.com/matplotlib/basemap/archive/v1.2.1rel.tar.gz

# Copy Python requirements
COPY python_requirements.txt .

# Install Python dependencies
RUN sudo pip install --no-cache-dir -r python_requirements.txt

# Set default workdir
WORKDIR $HOME
