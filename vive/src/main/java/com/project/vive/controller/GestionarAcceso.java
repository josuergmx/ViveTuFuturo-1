package com.project.vive.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.view.RedirectView;

@Controller
@RequestMapping("/login")
public class GestionarAcceso {
	@RequestMapping(method=RequestMethod.GET)
	public String login(){
		return "login";
	}
	@RequestMapping(method=RequestMethod.POST)
	public RedirectView verificarLogin(){
		return new RedirectView("redirect:/menu?nombre='Juan Castillo'");
	}
}
