Neoload load generator rpm package
==================================
QA_SKIP_BUILD_ROOT is needed is because of the underlying install4j installer which writes hard coded paths for some reason.
* Download sources: `spectool -g -R SPECS/neoload-7.6.0.spec`
* Build package: `QA_SKIP_BUILD_ROOT=1 rpmbuild -ba neoload-7.6.0.spec`
