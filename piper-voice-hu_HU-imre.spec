Name:		piper-voice-hu_HU-imre
Version:	2023.09.23
Release:	1
Summary:	Hungarian male voice for the Piper TTS system
URL:		https://huggingface.co/rhasspy/piper-voices/tree/main/hu/hu_HU/imre/medium
License:	MIT
BuildArch:	noarch
Group:		System/Multimedia
Provides:	piper-voice
Provides:	piper-voice-hu
Provides:	piper-voice-hu_HU

%sourcelist
https://huggingface.co/rhasspy/piper-voices/resolve/main/hu/hu_HU/imre/medium/hu_HU-imre-medium.onnx
https://huggingface.co/rhasspy/piper-voices/resolve/main/hu/hu_HU/imre/medium/hu_HU-imre-medium.onnx.json

%description
%{summary}

%install
mkdir -p %{buildroot}%{_datadir}/piper/voices
install -c -m 644 %{S:0} %{S:1} %{buildroot}%{_datadir}/piper/voices/

%files
%{_datadir}/piper/voices/*
