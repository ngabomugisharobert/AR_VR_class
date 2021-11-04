using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.Assertions;
using UnityEngine.SceneManagement;

public class PerkDemoUI : MonoBehaviour
{
  private bool m_inMenu;
  private GameObject m_cap;
  private OVRInput.Controller m_controller;

  void Start ()
  {
    Debug.Log("PERK starting the script");

     if( OVRPlugin.GetSystemHeadsetType() == OVRPlugin.SystemHeadset.Oculus_Go ){
      m_controller = OVRInput.Controller.RTrackedRemote;
      Debug.Log("PERK Oculus Go detected");
    }
    else if( OVRPlugin.GetSystemHeadsetType() == OVRPlugin.SystemHeadset.Oculus_Quest ){
      m_controller = OVRInput.Controller.RTouch;
      Debug.Log("PERK Oculus Quest detected");
    }
    else{
      Debug.Log("PERK **WARNING** unknown system headset type");
      Debug.Log("PERK **WARNING** no controller set!");
      m_controller = OVRInput.Controller.None;
    }

    DebugUIBuilder.instance.AddButton("PlaySound", ExecuteClick);
    DebugUIBuilder.instance.AddLabel("My Menu");

    DebugUIBuilder.instance.Show();
    m_inMenu = true;
	}

  void Update(){
    if(OVRInput.GetDown(OVRInput.Button.PrimaryIndexTrigger, m_controller) ){
        if(m_inMenu) DebugUIBuilder.instance.Hide();
        else DebugUIBuilder.instance.Show();
        m_inMenu = !m_inMenu;
    }

    /*
    //Below can be used to detect when a user depresses the Primary Touchpad
    if(OVRInput.GetDown(OVRInput.Button.PrimaryTouchpad, m_controller) ){
    }
    */
  }

  void ExecuteClick(){
    // The UI buttons from DebugUIBuilder are connected to the Primary Touchpad
    Debug.Log("PERK got the Primary Touchpad click");

    // Play a beep when clicked
    GameObject go_as = GameObject.Find("MySound");
    AudioSource aud_dat = go_as.GetComponent(typeof(AudioSource)) as AudioSource;
    aud_dat.Play(0);           
  }
}
