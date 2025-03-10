#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Library to enforce positional or key-word arguments
Summary(pl.UTF-8):	Biblioteka wymuszająca argumenty pozycyjne lub nazwane
Name:		python-positional
Version:	1.2.1
Release:	7
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/positional/positional-%{version}.tar.gz
# Source0-md5:	4afcffd8e2ba733fd7a50f137a2ee893
URL:		https://pypi.org/project/positional/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 1.8
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-fixtures >= 1.3.1
BuildRequires:	python-testrepository >= 0.0.18
BuildRequires:	python-testresources >= 0.2.4
BuildRequires:	python-testtools >= 1.4.0
BuildRequires:	python-wrapt >= 1.8
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-pbr >= 1.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-fixtures >= 1.3.1
BuildRequires:	python3-testrepository >= 0.0.18
BuildRequires:	python3-testresources >= 0.2.4
BuildRequires:	python3-testtools >= 1.4.0
BuildRequires:	python3-wrapt >= 1.8
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg-2 >= 1.2.1
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
positional provides a decorator which enforces only some args may be
passed positionally. The idea and some of the code was taken from the
oauth2 client of the google-api client.

%description -l pl.UTF-8
Moduł positional dostarcza dekorator wymuszający, aby tylko część
argumentów mogła być przekazana jako pozycyjne. Idea i część kodu
pochodzi z klienta oauth2 klienta google-api.

%package -n python3-positional
Summary:	Library to enforce positional or key-word arguments
Summary(pl.UTF-8):	Biblioteka wymuszająca argumenty pozycyjne lub nazwane
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-positional
positional provides a decorator which enforces only some args may be
passed positionally. The idea and some of the code was taken from the
oauth2 client of the google-api client.

%description -n python3-positional -l pl.UTF-8
Moduł positional dostarcza dekorator wymuszający, aby tylko część
argumentów mogła być przekazana jako pozycyjne. Idea i część kodu
pochodzi z klienta oauth2 klienta google-api.

%package apidocs
Summary:	API documentation for Python positional module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona positional
Group:		Documentation

%description apidocs
API documentation for Python positional module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona positional.

%prep
%setup -q -n positional-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}

rm -rf .testrepository
%endif

%if %{with python3}
%py3_build %{?with_tests:test}

rm -rf .testrepository
%endif

%if %{with doc}
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

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
%doc doc/build/html/{_static,api,*.html,*.js}
%endif
