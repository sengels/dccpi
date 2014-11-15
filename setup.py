"""
    Copyright (C) 2014  Hector Sanjuan

    This file is part of "dccpi".

    "dccpi" is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    "dccpi" is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup, Extension
setup(
    name="dccpi",
    packages=["dccpi"],
    version="1.0.0",
    description="A Python NMRA DCC protocol implementation for RaspberryPi",
    author="Hector Sanjuan",
    author_email="hector@convivencial.org",
    url="https://github.com/hsanjuan/dccpi",
    download_url="",
    license="GNU General Public License v3 (GPLv3)",
    keywords=["dcc", "nmra", "pi", "raspberry", "modelling",
              "train", "decoder"],
    install_requires=[
        'bitstring',
    ],
    ext_modules=[
        Extension('dcc_rpi_encoder_c',
                  sources=['extensions/dcc_rpi_encoder_c.c'],
                  libraries=['wiringPi'])
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Networking",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description="""\
==================================================================
NRMA Digital Command Control (DCC) implementation for Raspberry Pi
==================================================================

This module implements the DCC protocol for controlling model trains using a
Raspberry Pi.

It is able to output direction and speed DCC-encoded packets on one of the GPIO pins.

It is based on the:
 - `S-91 Electrical Standard <http://www.nmra.org/sites/default/files/standards/sandrp/pdf/s-9.1_electrical_standards_2006.pdf>`_
 - `S-92 DCC Communications Standard <http://www.nmra.org/sites/default/files/s-92-2004-07.pdf>`_

Please visit the github page for more information: https://github.com/hsanjuan/dccpi.
"""
)
