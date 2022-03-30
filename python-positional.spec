#
# Conditional build:
%bcond_with	doc	# build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Library to enforce positional or key-word arguments
Name:		python-positional
Version:	1.2.1
Release:	5
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/positional/positional-%{version}.tar.gz
# Source0-md5:	4afcffd8e2ba733fd7a50f137a2ee893
URL:		https://pypi.python.org/pypi/positional
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
positional provides a decorator which enforces only some args may be
passed positionally. The idea and some of the code was taken from the
oauth2 client of the google-api client.

%package -n python3-positional
Summary:	Library to enforce positional or key-word arguments
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-positional
positional provides a decorator which enforces only some args may be
passed positionally. The idea and some of the code was taken from the
oauth2 client of the google-api client.

%prep
%setup -q -n positional-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
rm -rf .testrepository
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/positional
%{py_sitescriptdir}/positional-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-positional
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/positional
%{py3_sitescriptdir}/positional-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
