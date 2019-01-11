Summary:	Mwclient is a client to the MediaWiki API
Name:		python-mwclient
Version:	0.9.3
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://sourceforge.net/apps/mediawiki/mwclient/index.php?title=Main_Page
Source0:	https://github.com/mwclient/mwclient/archive/v0.9.3/mwclient-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
Requires:	python-simplejson

%description
Mwclient is a client to the MediaWiki API <http://mediawiki.org/wiki/API>
and allows access to almost all implemented API functions

%files
%doc README.txt
%{py_puresitedir}/mwclient

%prep
%setup -qn mwclient-%{version}

%build
:

%install
install -d -m755 %{buildroot}%{py_puresitedir}/mwclient/
install -pm 0644 *.py %{buildroot}%{py_puresitedir}/mwclient/
