%global tl_name upca
%global tl_revision 22511

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Print UPC-A barcodes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/upca
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/upca.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/upca.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a single macro \upca, to print UPC-A barcodes.

