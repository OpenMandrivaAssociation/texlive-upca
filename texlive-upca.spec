# revision 22511
# category Package
# catalog-ctan /macros/generic/upca
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-upca
Version:	20140226
Release:	2
Summary:	Print UPC-A barcodes
URL:		http://www.ctan.org/tex-archive/macros/generic/upca
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upca.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upca.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a single macro \upca, to print UPC-A
barcodes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/upca/upca.tex
%doc %{_texmfdistdir}/doc/generic/upca/README
%doc %{_texmfdistdir}/doc/generic/upca/test-upca.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
