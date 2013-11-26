%define		packname	marray

Summary:	Exploratory analysis for two-color spotted microarray data
Name:		R-%{packname}
Version:	1.40.0
Release:	1
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	c82aa82073cdbc4cfb4839fb196d5082
URL:		http://bioconductor.org/packages/release/bioc/html/marray.html
BuildRequires:	R
BuildRequires:	R-limma
BuildRequires:	R-tkWidgets
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-limma
Suggests:	R-tkWidgets
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class definitions for two-color spotted microarray data. Fuctions for
data input, diagnostic plots, normalization and quality checking.

%prep
%setup -q -c -n %{packname}

%build
R CMD build %{packname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/swirldata
