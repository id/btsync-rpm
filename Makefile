.PHONY:	rpm clean

rpm:
	@mkdir -p SOURCES BUILD RPMS
	@cp bittorrent_sync*.tar.gz SOURCES/
	@rpmbuild -vv -bb --buildroot /tmp/btsync-rpm btsync.spec --define "version $(version)"

clean:
	@rm -rf SOURCES BUILD RPMS
