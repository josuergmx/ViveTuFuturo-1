package com.project.vive.repository;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.project.vive.entity.TipoDireccion;

@Repository("tipoDireccionRepository")
public interface TipoDireccionRepository extends JpaRepository<TipoDireccion, Serializable>{
	public abstract TipoDireccion findById(Integer id);
}
