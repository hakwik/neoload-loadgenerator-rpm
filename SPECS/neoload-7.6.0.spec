Name:		ub-neoload
Version:	7.6.0
Release:	0
Summary:	Neoload load generator	
Packager:	hakwik <hakan.wikstrom@kindredgroup.com>

Group:		Applications/Internet
License:	Commercial
URL:		https://www.neotys.com/
Source0:	https://d24mnm5myvorwj.cloudfront.net/documents/download/neoload/v7.6/neoload_7_6_0_linux_x64.sh
Source1:	neoload.varfile
Source3:	neoload.service
Prefix:         /opt/neoload-7.6.0
BuildRoot:      %{_tmppath}/%{name}-root

AutoReqProv:	no

BuildRequires:	fontconfig

# Don't break the Neoload jars
%define __jar_repack 0

# Installation directory when RPM is installed
%define nl_home /opt/neoload-7.6.0

%description
Neoload is a load testing tool. This is just the load generator part of the Neoload system.

%prep
cd %{_topdir}/BUILD
rm -f neoload*
cp -v %{_topdir}/SOURCES/neoload_7_6_0_linux_x64.sh .
cp -v %{_topdir}/SOURCES/neoload.varfile .

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
/usr/bin/bash neoload_7_6_0_linux_x64.sh -q -c -dir %{buildroot}%{nl_home} -varfile neoload.varfile
# /usr/bin/rm -rfv %{buildroot}%{nl_home}/.install4j
mkdir -p %{buildroot}/etc/systemd/system/
cp -v %{_topdir}/SOURCES/neoload.service %{buildroot}/etc/systemd/system/

%pre
# Create a "neoload" user and group if it doesn't already exist
/usr/bin/getent passwd neoload 2>&1 >/dev/null || /usr/sbin/useradd -c "Neoload user" -U -m -s /bin/bash -r -d /home/neoload neoload 2> /dev/null || /bin/true

%post
# (re-)create symlink for service script
/usr/bin/rm -f /opt/neoload
/usr/bin/ln -s %{nl_home} /opt/neoload

# Reload the systemd configuration
/usr/bin/systemctl daemon-reload
/usr/bin/systemctl enable neoload
/usr/bin/systemctl start neoload

%files
%{nl_home}/
/etc/systemd/system/neoload.service

%doc


%changelog

