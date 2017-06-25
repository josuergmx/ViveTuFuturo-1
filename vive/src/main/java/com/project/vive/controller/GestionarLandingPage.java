package com.project.vive.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
@RequestMapping("/inicio")
public class GestionarLandingPage {
	
	@RequestMapping(method=RequestMethod.GET)
	public String landingPage(){
		return "hola";
	}
}
