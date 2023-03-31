Name:		texlive-upca
Version:	22511
Release:	2
Summary:	Print UPC-A barcodes
URL:		http://www.ctan.org/tex-archive/macros/generic/upca
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upca.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upca.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
