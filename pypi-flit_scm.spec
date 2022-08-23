#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-flit_scm
Version  : 1.7.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/e2/99/961b062461652435b6ad9042d2ffdd75e327b36936987c2073aa784334d5/flit_scm-1.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e2/99/961b062461652435b6ad9042d2ffdd75e327b36936987c2073aa784334d5/flit_scm-1.7.0.tar.gz
Summary  : A PEP 518 build backend that uses setuptools_scm to generate a version file from your version control system, then flit to build the package.
Group    : Development/Tools
License  : MIT
Requires: pypi-flit_scm-license = %{version}-%{release}
Requires: pypi-flit_scm-python = %{version}-%{release}
Requires: pypi-flit_scm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(setuptools_scm)

%description
# flit_scm
A PEP 518 build backend that uses [`setuptools_scm`](https://github.com/pypa/setuptools_scm) to generate a version file from your version control system, then [`flit_core`](https://flit.readthedocs.io/en/latest/index.html) to build the package.

%package license
Summary: license components for the pypi-flit_scm package.
Group: Default

%description license
license components for the pypi-flit_scm package.


%package python
Summary: python components for the pypi-flit_scm package.
Group: Default
Requires: pypi-flit_scm-python3 = %{version}-%{release}

%description python
python components for the pypi-flit_scm package.


%package python3
Summary: python3 components for the pypi-flit_scm package.
Group: Default
Requires: python3-core
Provides: pypi(flit_scm)
Requires: pypi(flit_core)
Requires: pypi(setuptools_scm)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-flit_scm package.


%prep
%setup -q -n flit_scm-1.7.0
cd %{_builddir}/flit_scm-1.7.0
pushd ..
cp -a flit_scm-1.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657219845
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . flit-core
pypi-dep-fix.py . setuptools_scm
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . flit-core
pypi-dep-fix.py . setuptools_scm
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-flit_scm
cp %{_builddir}/flit_scm-1.7.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-flit_scm/29d3d7ebffdf889087bab0aad8b77f98e0beb6d9
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} flit-core
pypi-dep-fix.py %{buildroot} setuptools_scm
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-flit_scm/29d3d7ebffdf889087bab0aad8b77f98e0beb6d9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
