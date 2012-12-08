Name:           python-mwclient
Version:        0.6.5
Release:        %mkrel 2
Summary:        Mwclient is a client to the MediaWiki API
Group:          Development/Python
License:        MIT
URL:            http://sourceforge.net/apps/mediawiki/mwclient/index.php?title=Main_Page
Source0:        http://downloads.sourceforge.net/project/mwclient/mwclient/mwclient-%{version}/mwclient-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-simplejson

%description
Mwclient is a client to the MediaWiki API <http://mediawiki.org/wiki/API>
and allows access to almost all implemented API functions


%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/mwclient

# -------------------------------------------------------------------

%prep
%setup -q -n mwclient-%{version}

%build
:

%install
install -d -m755 %{buildroot}%{python_sitelib}/mwclient/
install -pm 0644 *.py %{buildroot}%{python_sitelib}/mwclient/


%clean
rm -rf %{buildroot}


%changelog
* Wed May 11 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.6.5-1mdv2011.0
+ Revision: 673594
- fix prep
- update to 0.6.5

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-3
+ Revision: 668007
- mass rebuild

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 0.6.4-2mdv2011.0
+ Revision: 591998
- Rebuild

* Sat Aug 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.4-1mdv2011.0
+ Revision: 567258
- update to 0.6.4

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6.3b-1mdv2010.1
+ Revision: 515908
- Update to 0.6.3b

* Fri Feb 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.3-1mdv2010.1
+ Revision: 504457
- import python-mwclient


