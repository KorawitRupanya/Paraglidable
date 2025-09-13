# Base image
FROM tensorflow/tensorflow:latest-py3

ARG USERNAME=paraglidable
RUN useradd -m $USERNAME
ENV HOME /home/$USERNAME

ENV DEBIAN_FRONTEND=noninteractive

ENV NPY_DISABLE_CPU_FEATURES=AVX,AVX2,FMA

# Install legacy system dependencies + basemap deps
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

# Configure sudo
RUN echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME && chmod 0440 /etc/sudoers.d/$USERNAME

# Upgrade pip (old version causes install failures)
RUN pip install --upgrade pip

USER $USERNAME
WORKDIR $HOME

# Upgrade pip (old version causes install failures)
RUN pip install --upgrade pip

# Install basemap 1.2.1 (from GitHub tarball)
RUN pip install https://github.com/matplotlib/basemap/archive/v1.2.1rel.tar.gz

# Copy Python requirements
COPY python_requirements.txt .

# Install Python packages (with sudo since USER is non-root)
RUN sudo pip install --no-cache-dir -r python_requirements.txt
