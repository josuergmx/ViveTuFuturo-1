package com.project.vive.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/hola")
public class HolaMundoController {
	@GetMapping("/mundo")
	public String holaMundo(){
		return "hola";
	}
}
