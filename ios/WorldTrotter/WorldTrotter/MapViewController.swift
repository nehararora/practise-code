//
//  MapViewController.swift
//  WorldTrotter
//
//  Created by Nehar Arora on 3/15/16.
//  Copyright © 2016 Nehar Arora. All rights reserved.
//

import UIKit
import MapKit

class MapViewController: UIViewController, MKMapViewDelegate {

    var mapView: MKMapView!
    var pins: [MKPointAnnotation]! = []
    var selectedPin: Int = 0
    
    override func loadView() {

        // create & set map view
        mapView = MKMapView()
        view = mapView

        // set delegate for user location
        mapView.delegate = self
        mapView.showsUserLocation = true

        // add segmented control for map type
        let segmentedControl = UISegmentedControl(items: ["Standard",
                    "hybrid",
                    "Satellite"])
        segmentedControl.backgroundColor = UIColor.whiteColor().colorWithAlphaComponent(0.5)
        segmentedControl.selectedSegmentIndex = 0

        segmentedControl.addTarget(self, action: "mapTypeChanged:", forControlEvents: .ValueChanged)

        segmentedControl.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(segmentedControl)

        // create constraints to match superview.
        let topConstraint = segmentedControl.topAnchor.constraintEqualToAnchor(topLayoutGuide.bottomAnchor, constant: 8)

        let margins = view.layoutMarginsGuide
        let leadingConstraint = segmentedControl.leadingAnchor.constraintEqualToAnchor(margins.leadingAnchor)
        let trailingConstraint = segmentedControl.trailingAnchor.constraintEqualToAnchor(margins.trailingAnchor)

        topConstraint.active = true
        leadingConstraint.active = true
        trailingConstraint.active = true

        // add user location button
        let locationButton = UIButton(type: UIButtonType.System) as UIButton
        locationButton.frame = CGRect(x: 30, y: 70, width: 75, height: 35)
        locationButton.setTitle("Center",forState: UIControlState.Normal)
        locationButton.backgroundColor = UIColor.blueColor().colorWithAlphaComponent(0.25)
        locationButton.addTarget(self, action: "scrollToUser:", forControlEvents: UIControlEvents.TouchUpInside)
        view.addSubview(locationButton)

        // add button to cycle pins
        let cycleButton = UIButton(type: UIButtonType.System)
        cycleButton.frame = CGRect(x: 110, y: 70, width: 75, height: 35)
        cycleButton.setTitle("cycle", forState: UIControlState.Normal)
        cycleButton.backgroundColor = UIColor.blueColor().colorWithAlphaComponent(0.25)
        cycleButton.addTarget(self, action: "cyclePins:", forControlEvents: UIControlEvents.TouchUpInside)
        view.addSubview(cycleButton)

        // drop pins...
        // delhi,
        let pin1: MKPointAnnotation = MKPointAnnotation()
        pin1.coordinate = CLLocationCoordinate2DMake(28.6139, 77.2090)
        pins.append(pin1)

        //piscataway,
        let pin2: MKPointAnnotation = MKPointAnnotation()
        pin2.coordinate = CLLocationCoordinate2DMake(40.5456, 74.4608)
        pins.append(pin2)

        // hawaii.
        let pin3: MKPointAnnotation = MKPointAnnotation()
        pin3.coordinate = CLLocationCoordinate2DMake(20.8000, 156.3333)
        pins.append(pin3)

        mapView.addAnnotations(pins)
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        print("mapController: I loads view")
    }

    func mapTypeChanged(segControl: UISegmentedControl){
        switch segControl.selectedSegmentIndex {
        case 0:
            mapView.mapType = .Standard
        case 1:
            mapView.mapType = .Hybrid
        case 2:
            mapView.mapType = .Satellite
        default:
            break
        }
    }

    func scrollToUser(sender: UIButton!) {
        print("scroll, scroll, scroll...")
        print("show user \(mapView.userLocation)...")
        //let userLocation = CLLocation(latitude: 21.282778, longitude: -157.829444)
        let userLocation = mapView.userLocation
        let coordinateRegion = MKCoordinateRegionMakeWithDistance(userLocation.coordinate, 5000, 5000)
        mapView.setRegion(coordinateRegion, animated: true)
    }

    func cyclePins(sender: UIButton!){
        let pin: MKAnnotation = pins[selectedPin]
        selectedPin = (++selectedPin % 3)

        let coordinateRegion = MKCoordinateRegionMakeWithDistance(pin.coordinate, 5000, 5000)
        mapView.setRegion(coordinateRegion, animated: true)
        print("cycle pins")
    }
}