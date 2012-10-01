"""
Dtella - Local Site Configuration
Copyright (C) 2007-2008  Dtella Labs (http://www.dtella.org/)
Copyright (C) 2007-2008  Paul Marks (http://www.pmarks.net/)
Copyright (C) 2007-2008  Jacob Feisley (http://www.feisley.com/)

$Id: local_config.py 610 2009-12-02 05:47:00Z sparkmaul $

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

# These settings are specific to the Purdue network.  They should be
# customized for each new network you create.

# Use this prefix for filenames when building executables and installers.
# It will be concatenated with the version number below.
build_prefix = "dtella-vt-"

# Dtella version number.
version = "2012.10.01"

# This is an arbitrary string which is used for encrypting packets.
# It essentially defines the uniqueness of a Dtella network, so every
# network should have its own unique key.
network_key = 'VirginiaTechDtella-58'

# This is the name of the "hub" which is seen by the user's DC client.
# "Dtella@____" is the de-facto standard, but nobody's stopping you
# from picking something else.
hub_name = "Dtella@VirginiaTech"

# This enforces a maximum cap for the 'minshare' value which appears in DNS.
# It should be set to some sane value to prevent the person managing DNS from
# setting the minshare to 99999TiB, and effectively disabling the network.
minshare_cap = 100 * (1024**3)   # (=100GiB)

# This is a list of subnets (in CIDR notation) which will be permitted on
# the network.  Make sure you get this right initially, because you can't
# make changes once the program has been distributed.  In the unlikely event
# that you don't want any filtering, use ['0.0.0.0/0']
allowed_subnets = ['198.82.0.0/16', '128.173.0.0/16', '172.16.0.0/12', '192.70.138.0/24', '192.70.187.0/24']
#allowed_subnets = ['198.82.56.0/21', '198.82.64.0/18', '128.173.32.0/21']

# Here we configure an object which pulls 'Dynamic Config' from some source
# at a known fixed location on the Internet.  This config contains a small
# encrypted IP cache, version information, minimum share, and a hash of the
# IRC bridge's public key.

# -- Use Google Spreadsheet --
import dtella.modules.pull_gdata
dconfig_puller = dtella.modules.pull_gdata.GDataPuller(
   sheet_key = "0AgyUNeuFyTgudDY2Q0x6Q0J1aVV4ZkcyUzRiSjF6UWc"
   )

# Enable this if you can devise a meaningful mapping from a user's hostname
# to their location.  Locations are displayed in the "Connection / Speed"
# column of the DC client.
use_locations = True

###############################################################################

# if use_locations is True, then rdns_servers and hostnameToLocation will be
# used to perform the location translation.  If you set use_locations = False,
# then you may delete the rest of the lines in this file.

# DNS servers which will be used for doing IP->Hostname reverse lookups.
# These should be set to your school's local DNS servers, for efficiency.
rdns_servers = ['198.82.247.66','198.82.247.98','198.82.247.34']

# Customized data for our implementation of hostnameToLocation
import re
#dorm_re = re.compile(r."^([a-z]{1}[0-9a-fA-F]{6}).*\..*\.vt\.edu$")
dhcp_re = re.compile(r"^(h[a-z0-9]{6}).*\.dhcp\.vt\.edu$")
wifi_re = re.compile(r"^(n[a-z0-9]{6}).*\.cns\.vt\.edu$")
suffix_re = re.compile(r".*\.([^.]+)\.vt\.edu$")
prefix_re = re.compile(r"^([a-z]{2}).*\..*\.vt\.edu$")
	
pre_table = {
	'bioi'			: "Bioinformatics",

    'h80ad'         : "DHCP - Unknown Department"
}

dhcp_table = {
    # dorms
    'hc65238'       : "Barringer Hall",
    'hc65239'       : "Barringer Hall",
    'hc6523a'       : "Vawter Hall",
    'hc6523b'       : "Vawter Hall",
    'hc6523c'       : "Main Egg. Hall",
    'hc6523d'       : "Main Egg. Hall",
    'hc6523e'       : "Newman Hall",
    'hc6523f'       : "Newman Hall",
    'hc65240'       : "Monteith Hall",
    'hc65241'       : "Monteith Hall",
    'hc65242'       : "Rasche Hall",
    'hc65243'       : "Rasche Hall",
                    # 198.82.68.0/23 - unused?
    'hc65246'       : "Thomas Hall",
    'hc65247'       : "Thomas Hall",
    'hc65248'       : "Brodie Hall",
    'hc65249'       : "Brodie Hall",
    'hc6524a'       : "West Egg. Hall",
    'hc6524b'       : "West Egg. Hall",
    'hc6524c'       : "SPB",
    'hc6524d'       : "SPG",
    'hc6524e'       : "Harper Hall",
    'hc6524f'       : "Harper Hall",
    'hc65250'       : "East Campbell",
    'hc65251'       : "Hillcrest Hall",
    'hc65252'       : "Main Campbell Hall",
    'hc65253'       : "Slusher Tower",
    'hc65254'       : "Slusher Tower",
    'hc65255'       : "Slusher Hall",
    'hc65256'       : "Slusher Hall",
    'hc65257'       : "Slusher Hall",
    'hc65258'       : "Cochrane Hall",
    'hc65259'       : "Cochrane Hall",
    'hc6525a'       : "Cochrane Hall",
    'hc6525b'       : "East Ambler Johnston Hall", #??
    'hc6525c'       : "East Ambler Johnston Hall", #??
    'hc6525d'       : "East Ambler Johnston Hall", #??
    'hc6525e'       : "Johnson Hall",
    'hc6525f'       : "Lee Hall", 
    'hc65260'       : "Lee Hall", 
    'hc65261'       : "Lee Hall", 
    'hc65262'       : "Lee Hall", 
    'hc65263'       : "Lee Hall", 
                    #198.82.100.0/23 - ??
    'hc65266'       : "New Residence Hall East", 
    'hc65267'       : "New Residence Hall East", 
    'hc65268'       : "Peddrew-Yates Hall",
    'hc65269'       : "Peddrew-Yates Hall",
    'hc6526a'       : "Payne Hall",
    'hc6526b'       : "Payne Hall", 
    'hc6526c'       : "Pritchard Hall", 
    'hc6526d'       : "Pritchard Hall", 
    'hc6526e'       : "Pritchard Hall", 
    'hc6526f'       : "Pritchard Hall", 
    'hc65270'       : "Pritchard Hall", 
    'hc65271'       : "Pritchard Hall", 
    'hc65272'       : "Pritchard Hall", 
    'hc65273'       : "West Ambler Johnston Hall", 
    'hc65274'       : "West Ambler Johnston Hall", 
    'hc65275'       : "West Ambler Johnston Hall", 
    'hc65276'       : "West Ambler Johnston Hall", 
    'hc65277'       : "West Ambler Johnston Hall", 
    'hc65278'       : "West Ambler Johnston Hall", 
    'hc65279'       : "Miles Hall", 
    'hc6527a'       : "Miles Hall", 
    'hc6527b'       : "SPK", 
    'hc6527c'       : "SPO", 
    'hc6527d'       : "Donaldson Brown", 
    'hc6527e'       : "New Hall West", 
    'hc6527f'       : "New Hall West"
}


suf_table = {
	# routers
	'bur'			: "Burruss",
	'cas'			: "Cassell",
	'hil'			: "Hillcrest",
	'isb'			: "ISB",
	'sha'			: "Shanks",
    'owe'           : "Owens",

	# buildings
	'fralin'		: "Fralin Biotechnology Center",
	'glc'			: "Graduate Life Center",

	# departments
	'acm'			: "Association for Computing Machinery",
	'admiss'		: "Admissions",
	'alumni'		: "Alumni Association",
	'arch'			: "Architecture",
	'ag'			: "College of Agriculture",
	'aoe'			: "Aerospace and Ocean Engineering",
	'arc'			: "Advanced Research Computing",
	'ath'			: "Athletics",
	'biochem'		: "Biochemistry",
	'bioinformatics': "Bioinformatics",
	'biol'			: "Biology",
	'bit'			: "Business Information Technology",
	'bursar'		: "Bursar's Office",
	'cc'			: "Computing Center",
	'cee'			: "Civil and Environmental Engineering",
	'coe'			: "College of Engineering",
	'che'			: "Chemical Engineering",
	'chem'			: "Chemistry",
	'cirt'			: "Computer Incident Response Team",
	'clah'			: "College of Liberal Arts and Human Sciences",
	'comm'			: "Communications Studies",
	'cos'			: "College of Science",
	'cs'			: "Computer Science",
	'dsa'			: "Division of Student Affairs",
	'ece'			: "Electrical and Computer Engineering",
	'econ'			: "Economics",
	'edtech'		: "Educational Technology",
	'emergency'		: "Emergency Management",
	'emporium'		: "Math Emporium",
	'enge'			: "Engineering Education",
	'english'		: "English",
	'engr'			: "Engineering",
	'esm'			: "Engineering Science and Mechanics",
	'facilities'	: "Facilities",
	'finaid'		: "Financial Aid",
	'fll'			: "Foreign Language",
	'fs'			: "Fleet Services",
	'geog'			: "Geography",
	'geos'			: "Geosciences",
	'grads'			: "Graduate School",
	'hist'			: "History",
	'honors'		: "Honors Program",
	'hs'			: "Honor System",
	'ictas'			: "Institute for Critical Technology and Applied Sciences",
	'ipg'			: "Institute for Policy and Governance",
	'it'			: "Information Technology",
	'its'			: "Information Technology Support",
	'is'			: "InnovationSpace",
	'lt'			: "Learning Technologies",
	'mailservices'	: "Mail Services",
	'math'			: "Mathematics",
	'me'			: "Mechanical Engineering",
	'mine'			: "Mining and Minerals Engineering",
	'music'			: "Music",
	'phil'			: "Philosophy",
	'phys'			: "Physics",
	'ppws'			: "Plant Pathology and Weed Science",
	'police'		: "Police Department",
	'psci'			: "Political Science",
	'pres'			: "President's Office",
	'print'			: "Printing Services",
	'provost'		: "Provost",
	'psyc'			: "Psychology",
	'registrar'		: "Registrar's Office",
	'rescue'		: "VT Rescue",
	'soc'			: "Sociology",
	'ssd'			: "Services for Students with Diabilities",
	'vetmed'		: "College of Veterinary Medicine",
	'vpas'			: "Administrative Services",
	'vtc'			: "School of Medicine",
	'vtcc'			: "Corps of Cadets",
	'vtes'			: "Virginia Tech Electric Service",
	'vtip'			: "Virginia Tech Intellectual Properties",
	'vtti'			: "Virginia Tech Transportation Institute",

	# other
	'async' 		: "VPN",
	#'dhcp'  		: "Residence Hall",
}

def hostnameToLocation(hostname):
    # Convert a hostname into a human-readable location name.

    if hostname:
        # Try dorms first
        dhcp = dhcp_re.match(hostname)
        if dhcp:
            try:
                return dhcp_table[dhcp.group(1)]
            except KeyError:
                pass

        wifi = wifi_re.match(hostname)
        if wifi:
            return "Wireless"

        suffix = suffix_re.match(hostname)
        if suffix:
            try:
                return suf_table[suffix.group(1)]
            except KeyError:
                pass
        
        prefix = prefix_re.match(hostname)
        if prefix:
            try:
                return pre_table[prefix.group(1)]
            except KeyError:
                pass


    return "Unknown"

