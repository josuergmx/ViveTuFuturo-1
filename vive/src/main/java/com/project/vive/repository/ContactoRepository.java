package com.project.vive.repository;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.project.vive.entity.Contacto;

@Repository("contactoRepository")
public interface ContactoRepository extends JpaRepository<Contacto, Serializable>{
	public abstract Contacto findByCelular(Integer celular);
	public abstract Contacto findByEmail(String email);
}
