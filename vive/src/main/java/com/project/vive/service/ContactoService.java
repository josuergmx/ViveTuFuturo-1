package com.project.vive.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.project.vive.entity.Contacto;
import com.project.vive.repository.ContactoRepository;
import com.project.vive.service.impl.ContactoImpl;

@Service("contactoService")
public class ContactoService implements ContactoImpl{
	
	@Autowired
	@Qualifier("contactoRepository")
	ContactoRepository contactoRepository;
	
	@Override
	public Contacto guardar(Contacto model) {
		contactoRepository.save(model);
		return null;
	}

}
