srpm:
	dnf install -y /usr/bin/spectool /usr/bin/rpkg
	spectool -ag -C $(outdir) $(spec)
	rpkg srpm --spec $(spec) --outdir $(outdir)
