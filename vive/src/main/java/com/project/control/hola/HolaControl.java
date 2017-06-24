package com.project.control.hola;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HolaControl {
	
	@RequestMapping("/hola")//Solo responde con metodos get
	public String hola(){
		return "hola";
		
	}
}
