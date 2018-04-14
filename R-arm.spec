#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-arm
Version  : 1.10.1
Release  : 7
URL      : https://cran.r-project.org/src/contrib/arm_1.10-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/arm_1.10-1.tar.gz
Summary  : Data Analysis Using Regression and Multilevel/Hierarchical
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Matching
Requires: R-abind
Requires: R-coda
Requires: R-lme4
Requires: R-survey
BuildRequires : R-Matching
BuildRequires : R-abind
BuildRequires : R-coda
BuildRequires : R-lme4
BuildRequires : R-survey
BuildRequires : clr-R-helpers

%description
# arm
ARM: Data Analysis Using Regression and Multilevel/Hierarchical Models

%prep
%setup -q -c -n arm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523729177

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523729177
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library arm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library arm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library arm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library arm|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/arm/DESCRIPTION
/usr/lib64/R/library/arm/INDEX
/usr/lib64/R/library/arm/Meta/Rd.rds
/usr/lib64/R/library/arm/Meta/data.rds
/usr/lib64/R/library/arm/Meta/features.rds
/usr/lib64/R/library/arm/Meta/hsearch.rds
/usr/lib64/R/library/arm/Meta/links.rds
/usr/lib64/R/library/arm/Meta/nsInfo.rds
/usr/lib64/R/library/arm/Meta/package.rds
/usr/lib64/R/library/arm/NAMESPACE
/usr/lib64/R/library/arm/R/arm
/usr/lib64/R/library/arm/R/arm.rdb
/usr/lib64/R/library/arm/R/arm.rdx
/usr/lib64/R/library/arm/data/lalonde.rda
/usr/lib64/R/library/arm/help/AnIndex
/usr/lib64/R/library/arm/help/aliases.rds
/usr/lib64/R/library/arm/help/arm.rdb
/usr/lib64/R/library/arm/help/arm.rdx
/usr/lib64/R/library/arm/help/paths.rds
/usr/lib64/R/library/arm/html/00Index.html
/usr/lib64/R/library/arm/html/R.css
