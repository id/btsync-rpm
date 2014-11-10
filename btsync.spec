%define _topdir %(echo $PWD)

Name:           btsync
Version:        %{version}
Release:        1
Summary:        BitTorrent Sync - an application for data synchronization
Vendor:         BitTorrent Inc.
URL:            http://www.bittorrent.com/sync/
Packager:       Ivan Dyachkov <ivan@dyachkov.org>
License:        http://www.bittorrent.com/legal/eula
Source:         bittorrent_sync_x64.tar.gz

%description
http://sync-help.bittorrent.com/

%prep
%setup -c
cp %{_topdir}/init ./
cp %{_topdir}/btsync_users ./

%build

%install
install -D btsync %{buildroot}/usr/local/bin/btsync
install -D init %{buildroot}/etc/rc.d/init.d/btsync
touch %{buildroot}/etc/btsync_users

%post
if [ $1 = 1 ]; then
    /sbin/chkconfig --add btsync
fi

%preun
# When the last version of a package is erased, $1 is 0
if [ $1 = 0 ]; then
    /sbin/service btsync stop
    /sbin/chkconfig --del btsync
fi

%postun
# When the last version of a package is erased, $1 is 0
# Otherwise it's an upgrade and we need to restart the service
if [ $1 -ge 1 ]; then
    /sbin/service btsync stop >/dev/null 2>&1
    sleep 1
    /sbin/service btsync start >/dev/null 2>&1
fi

%files
/usr/local/bin/btsync
/etc/rc.d/init.d/btsync
%doc README
%doc LICENSE.TXT
%config /etc/btsync_users
