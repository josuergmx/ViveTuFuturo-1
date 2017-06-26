package com.project.vive.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("/menu")
public class GestionarDashboard {
	@RequestMapping(method = RequestMethod.GET)
	public ModelAndView dashboard(@RequestParam(name="nombre", defaultValue="Juan Castillo")String nombre) {
		ModelAndView mav =  new ModelAndView("dashboard");
		mav.addObject("nombre",nombre);
		return mav;
	}
	
}
