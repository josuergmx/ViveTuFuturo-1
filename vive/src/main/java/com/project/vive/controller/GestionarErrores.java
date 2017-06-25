package com.project.vive.controller;

import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GestionarErrores {
	//En este caso se usa la exception generica, despues se cambiará por particulares
	@ExceptionHandler(Exception.class)
	public String clasificarError(){
		return "error/500";
	}
}
