Summary:	Mwclient is a client to the MediaWiki API
Name:		python-mwclient
Version:	0.10.1
Release:	2
Group:		Development/Python
License:	MIT
Url:		http://sourceforge.net/apps/mediawiki/mwclient/index.php?title=Main_Page
Source0:	https://files.pythonhosted.org/packages/97/b4/5fc70ad3286a8d8ec4b9ac01acad0f6b00c5a48d4a16b9d3be6519b7eb21/mwclient-0.10.1.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
Requires:	python-simplejson

%description
Mwclient is a client to the MediaWiki API <http://mediawiki.org/wiki/API>
and allows access to almost all implemented API functions

%files
%{python_sitelib}/mwclient

%prep
%setup -qn mwclient-%{version}

%build
:

%install
install -d -m755 %{buildroot}%{python_sitelib}/mwclient/
install -pm 0644 *.py %{buildroot}%{python_sitelib}/mwclient/

